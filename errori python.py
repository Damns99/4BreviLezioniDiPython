###Errori comuni

##sintax error

#syntax error è l'errore che appare ogni qualvolta che un comando viene scritto male o viene usato un carattere sbagliato, qui sono riportati alcuni esempi

#print("ciao')

'''
d=5
print("f=%f", %d)
'''

#impord numpy
'''
import numpy 
a=numpy.array(dtype=int , [1,1,1,1,1,1,1])
'''
'''
import numpy
a=numpy.array([1,1,1,1,1,1,1], dtype=2 ,dtype=2)
'''

##dividere per zero

'''
import numpy

a=numpy.array([1,2,5,9,0,7,3])

b=1/a
'''

##array di diverse lunghezze

'''
import numpy

a=numpy.array([1,2,5,9,8,7,3])
b=numpy.array([15,8,6,7])

c=a+b
'''

##File not found
'''
import pylab

x, Dx, y, Dy = pylab.loadtxt('dati4.txt', unpack=True)
'''

## index out of bound

'''
import numpy

a=numpy.array([1,1,1,1,1,1,1,1,1,1,1,1])

n=a[12]
'''

## indentation error
'''
def funzione(x, a, b):
return a*x+b


def funzione(x, a, b):m
    return a*x+b
    
n=5
f=9
x=3

h=funzione(x,n,f)
print(h)
'''

## errori di scrittura

'''
import numpy
import pylab

plt.figure(1)
def f(x):
    return x**3
x = np.linspace(-1, 1, 1000)

plt.plot(x, f(x))
plt.show(figure=1)
'''

'''
import numpy
a=numpy.array([1,1,1,1,1,1,1], dtype=6)
'''

'''
import numpy
a=numpy.array([1,1,1,1,1,1,1], unpack=True)
'''
##errori di definizione

'''
x=3
b=x+g
print(b)
'''









