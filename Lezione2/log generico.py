import pylab
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

## Dati dal file.
x, dx, y, dy = pylab.loadtxt('dati log.txt', unpack = True)

##Modello
def model(x, m,q):
    return m*x+q
    
##Funzione Propagazione Errori
def errlog(x,dx):
    return 1/numpy.log(10)*dx/x

##Trasformiamo X e Y nei loro logaritmi
xx=numpy.log10(x)
yy=numpy.log10(y)
dxx=errlog(x,dx)
dyy=errlog(y,dy)

##Determino i migliori valori di M e q 
pars, covm = curve_fit(model, xx, yy, sigma=dyy, absolute_sigma=False)
print('m  = %.5f +- %.5f ' % (pars[0], numpy.sqrt(covm.diagonal()[0])))
print('q  = %.5f +- %.5f ' % (pars[1], numpy.sqrt(covm.diagonal()[1])))


##Grafico principale

plt.figure(1)
plt.plot(xx,yy,'.',markersize=1,color='black')
plt.errorbar(xx, yy, dyy, dxx, fmt='none', ecolor='black')
X=numpy.linspace(0,numpy.max(xx), 10)
plt.plot(X,model(X, *pars), color='blue', alpha=0.5)
plt.grid()

##Modello
def model1(x, m,q, e):
    return m*x**e+q


##Determino i migliori valori di M e q 
pars, covm = curve_fit(model1, x, y, sigma=dy, absolute_sigma=False)
print('m  = %.5f +- %.5f ' % (pars[0], numpy.sqrt(covm.diagonal()[0])))
print('q  = %.5f +- %.5f ' % (pars[1], numpy.sqrt(covm.diagonal()[1])))
print('e  = %.5f +- %.5f ' % (pars[2], numpy.sqrt(covm.diagonal()[2])))

##Grafico in carta bilogaritmica
plt.figure(2)
plt.errorbar(x, y, dy, dx,linestyle='', ecolor='black')
X=numpy.logspace(0.2,2, 1000)
plt.loglog(X,model1(X, *pars), color='blue')
plt.grid()

plt.show()