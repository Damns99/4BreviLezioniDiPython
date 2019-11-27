import pylab
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

## Dati dal file.
x, dx, y, dy = pylab.loadtxt('Dati.txt', unpack = True)

##Modello
def model(x, m,q):
    return m*x+q

#Determino i migliori valori di m e q 
pars, covm = curve_fit(model, x, y,  sigma=dy, absolute_sigma=False)
print('m  = %.5f +- %.5f ' % (pars[0], numpy.sqrt(covm.diagonal()[0])))
print('q  = %.5f +- %.5f ' % (pars[1], numpy.sqrt(covm.diagonal()[1])))


##Grafico principale
plt.plot(x,y,'.',markersize=1,color='black')
plt.errorbar(x, y, dy, dx, fmt='none', ecolor='black')
x=numpy.linspace(0,numpy.max(x)+1, 10)
y=model(x, *pars)
plt.plot(x,y, color='blue', alpha=0.5)
plt.grid()

plt.show()