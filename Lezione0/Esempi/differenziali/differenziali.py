import numpy as np
import pylab

def der2(x,y,d1):
    return -np.sin(y)-0.05*d1
'''
def der(x,y):
    return 1
'''
def orizz(x,y):
    return x/x*y
    
def Ripeti(i,passo,rip):
    p, q, r = i
    x=np.array([p])
    y=np.array([q])
    d1=np.array([r])
    for k in range(0,rip-1):
        dm=der2(x[k],y[k],d1[k])
        m=d1[k]+dm*passo
        newx=x[k]+passo
        newy=y[k]+m*passo
        if(newy>100 or newy<-100):
            break
        x=np.append(x,newx)
        y=np.append(y,newy)
        d1=np.append(d1,m)
    pylab.plot(x,y,linewidth='1')


condizioni=[(0.,i/2.5,0.) for i in range(0,5)]
#condizioni=[(0.,0.,i/5+4) for i in range(-5,5)]
#condizioni=[(0.,1.,0.)]

ics=np.linspace(-10,10,10000)

#tempi positivi
for i in condizioni:
    Ripeti(i,0.01,5000)
#tempi negativi
for i in condizioni:
    Ripeti(i,-0.01,0)

pylab.grid()
pylab.show()