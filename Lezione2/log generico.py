import pylab
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

## Dati dal file.
x, dx, y, dy = pylab.loadtxt('dati log.txt', unpack = True)

##Modello lineare
def model(x, m,q):
    return m*x+q

##Modello quadratico
def model1(x, m,q, e):
    return m*x**e+q
    
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

##Determino i migliori valori di m, q, e
pars1, covm1 = curve_fit(model1, x, y, sigma=dy, absolute_sigma=False)
print('m1 = %.5f +- %.5f ' % (pars1[0], numpy.sqrt(covm1.diagonal()[0])))
print('q1  = %.5f +- %.5f ' % (pars1[1], numpy.sqrt(covm1.diagonal()[1])))
print('e  = %.5f +- %.5f ' % (pars1[2], numpy.sqrt(covm1.diagonal()[2])))


##Grafico principale

plt.figure(1)
plt.subplot(212)
plt.plot(xx,yy,'.',markersize=1,color='black')
plt.errorbar(xx, yy, dyy, dxx, fmt='none', ecolor='black')
X=numpy.linspace(0,numpy.max(xx), 10)
plt.plot(X,model(X, *pars), color='blue', alpha=0.5)
plt.grid()

plt.subplot(211)
plt.plot(x,y,'.',markersize=1,color='black')
plt.errorbar(x, y, dy, dx, fmt='none', ecolor='black')
X=numpy.linspace(0,numpy.max(x), 1000)
plt.plot(X,model1(X, *pars1), color='blue', alpha=0.5)
plt.grid()

plt.show()


##Grafico in carta bilogaritmica
plt.figure(2)
plt.errorbar(x, y, dy, dx,linestyle='', ecolor='black')
X=numpy.logspace(0.2,2, 1000)
plt.loglog(X,model1(X, *pars1), color='blue')
plt.grid()

plt.show()