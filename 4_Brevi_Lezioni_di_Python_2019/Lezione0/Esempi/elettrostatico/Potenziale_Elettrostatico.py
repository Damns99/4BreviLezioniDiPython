import pylab as pl
import numpy as np
from matplotlib import colors

#Cariche puntiformi e loro posizioni (è possibile simulare distribuzioni per punti)
Q=pl.array([-1, 2, 0.5])
X=pl.array([-2, 2, 0])
Y=pl.array([0, 0, 2])

X=np.array(X)
Y=np.array(Y)
Q=np.array(Q)

def potenziale(xp, yp):
    p=Q/((X-xp)**2+(Y-yp)**2)
    return pl.sum(p)
    
DELTA=0.1
dist=5

xmin=X.mean()-dist
xmax=X.mean()+dist
ymin=Y.mean()-dist
ymax=Y.mean()+dist

M=[]
a=[]
b=[]

maxval=1

for i in range(0, int((ymax-ymin)/DELTA)):
    val=potenziale(xmin, ymin+i*DELTA)
    if val>maxval:
        val=maxval
    elif val<-maxval:
        val=-maxval
    A=[val]
    
    for j in range(1, int((xmax-xmin)/DELTA)):
        val=potenziale(xmin+j*DELTA, ymin+i*DELTA)
        if val>maxval:
            val=maxval
        elif val<-maxval:
            val=-maxval
    
        if val*A[len(A)-1]<=0:
            a.append(xmin+j*DELTA)
            b.append(-(ymin+i*DELTA))
            
        A.append(val)
        
    M.append(A)

##Linee di annullamento del potenziale
pl.figure(0)
pl.scatter(a, b, marker='.')
pl.scatter(X, -Y, c='red')
pl.axis('equal')

M=pl.matrix(M)

##Mappa del potenziale
pl.figure(1)
mappa=colors.LinearSegmentedColormap.from_list('Potenziale', [(0, 'blue'), (0.5, 'white'), (1, 'red')], 256)
imm=pl.imshow(M, interpolation='nearest', cmap=mappa)
pl.colorbar(imm, cmap=mappa)

pl.show()
