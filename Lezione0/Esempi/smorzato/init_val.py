import pylab
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fit_function(x, omega):
    """ Definition of the fit function.
    """
    return pylab.sin(omega*x)

# Load the data from the file.
t, s, ds = pylab.loadtxt('roba.txt', unpack = True)

# Define a grid and calculate the values of the chisquare on the grid
# (note we are not fitting, here).
omega_grid = numpy.linspace(0, 10, 500)
chi2_values = []
for omega in omega_grid:
    chi2 = (((s - fit_function(t, omega))/ds)**2).sum()
    chi2_values.append(chi2)

# Make a plot of the chisquare as a function of omega.
#pylab.rc('font', size = 18)
#pylab.title('Chisquare scan', y = 1.02)
#pylab.xlabel('omega [1/s]')
#pylab.ylabel('chisquare', labelpad = 0)
#pylab.grid(color = 'gray')
#pylab.plot(omega_grid, chi2_values, color = 'black')

popt, pcov = curve_fit(fit_function, t, s, sigma=ds) #li passo col nome se li metto non in ordine
print('popt = %s' % popt) #valori ottimali parametri
print('pcov = \n %s\n' % pcov) #sulla diagonale ha la varianza (covarianza di ciascuna x con se stessa)

omega0 = popt #tanto per chiamarli per nome
domega = numpy.sqrt(pcov.diagonal()) #dev standard (sqrt varianza)
print('m = %.3f +- %.2f' % (omega0, domega))

chisq = sum(((s - fit_function(s, omega0))/ds)**2.) #grazie numpy che fa operazioni per elementi sui vettori...
print('chisq = %3f' % chisq)

x = numpy.linspace(0, 20, 100) #griglia
y = fit_function(x, omega0) #potevo fare anche straight_line(x, *popt) perché * spacchetta

plt.errorbar(t, s, ds, fmt='o') #fmt='o' sennò collega i punti
plt.plot(x, y)

# Finally: show the plot on the screen.
pylab.grid()
pylab.show()