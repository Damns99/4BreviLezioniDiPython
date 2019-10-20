import numpy
import pylab as plt
a=10000
x=numpy.random.rand(a)
y=numpy.random.rand(a)
cont=0


for n in range(len(x)):

    if (numpy.sqrt(x[n]**2+y[n]**2)<1):
        cont=cont+1
        print(str(n/a*100)+'%')
        fig1 = plt.figure(1)
        frame1=fig1.add_axes((.1,.1,.8,.8))
        plt.plot(x[n],y[n],'.',color='red')
    else:
        fig1 = plt.figure(1)
        frame1=fig1.add_axes((.1,.1,.8,.8))
        plt.plot(x[n],y[n],'.',color='black')


print((4*cont/a), 1/numpy.sqrt(a))
plt.grid(True)
plt.show()

'''
for n in range(len(a)):

    #if (numpy.sqrt(x[n]**2+y[n]**2)<1):
    if (y[n]<1/numpy.sqrt(2*3.14)*numpy.exp(-(x[n]**2/2))):
        cont=cont+1
        print(str(n/a*100)+'%')
        fig1 = plt.figure(1)
        frame1=fig1.add_axes((.1,.1,.8,.8))
        plt.plot(x[n],y[n],'.',color='red')
    else:
        fig1 = plt.figure(1)
        frame1=fig1.add_axes((.1,.1,.8,.8))
        plt.plot(x[n],y[n],'.',color='black')


print((4.8*cont/a), 1/numpy.sqrt(a))
plt.grid(True)
plt.show()
'''