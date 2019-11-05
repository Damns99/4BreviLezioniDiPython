import pylab
import numpy as np
import math
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.odr import odrpack

r=pylab.array([1.115, 0.9125, 0.8330, 0.7140, 0.6340])
dr=pylab.array(len(r)*[0.003], 'd')
macciaio=pylab.array([ 44.813, 24.757, 18.910, 11.975, 8.433], 'd')
Dmacciaio = pylab.array(len(macciaio)*[0.005],'d')

def f3(x,p3, e):
    return p3*(4/3)*(x**e)*(3.14)
    
popt, pcov = curve_fit(f3, r, macciaio, pylab.array([3., 7.7]), sigma=Dmacciaio, absolute_sigma=False)
p3, e= popt
dp3, de= pylab.sqrt(pcov.diagonal())
p4=p3*1000
dp4=dp3*1000
chisq2=np.sum(((macciaio-f3(r,p3,e))/Dmacciaio)**2) #Chiquadro

print('ACCIAIO SFERE')
print('Chiquadro = %f' %(chisq2))
print('Densita : %.2f+-%.2f'%(p4,dp4))
print('Esponente della legge di potenza: %.5f +- %.5f' %(e, de))

xx= np.linspace(0.5, 1.2, 1000)
pylab.figure(5)
pylab.subplot(211)
pylab.title('Massa delle sfere in funzione del loro raggio')
pylab.ylabel('Massa [g]')
plt.grid(True, which= 'both', color = 'gray')
pylab.errorbar(r, macciaio, Dmacciaio, dr, 'o', color='red' )
pylab.loglog(xx, f3(xx, p3, e), color='blue', label = 'Acciaio' )
#pylab.xticks([0.5,  0.7, 0.8, 0.9, 1.0, 1.1])
pylab.legend()

pylab.subplot(212)
pylab.grid(color='gray')
pylab.xlabel('Raggio [cm]')
pylab.ylabel('Residui [g]')
pylab.errorbar(r, macciaio-f3(r, p3, e), Dmacciaio, 0, 'o', color='blue' )


pylab.show()