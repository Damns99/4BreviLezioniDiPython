import pylab as pl
from matplotlib import colors

Q=pl.array([-1, 4])
X=pl.array([-2, 2])
Y=pl.array([0, 0])

def potenziale(xp, yp):
    p=Q/((X-xp)**2+(Y-yp)**2)
    return pl.sum(p)
    
DELTA=0.01

xmin=-8
xmax= 4

ymin=-4
ymax= 4

M=[]
a=[]
b=[]

for i in range(0, int((ymax-ymin)/DELTA)):
    val=potenziale(xmin, ymin+i*DELTA)
    if val>1:
        val=1
    elif val<-1:
        val=-1
    A=[val]
    
    for j in range(1, int((xmax-xmin)/DELTA)):
        val=potenziale(xmin+j*DELTA, ymin+i*DELTA)
        if val>1:
            val=1
        elif val<-1:
            val=-1
    
        if val*A[len(A)-1]<=0:
            a.append(xmin+j*DELTA)
            b.append(-(ymin+i*DELTA))
            
        A.append(val)
        
    M.append(A)
    
pl.figure(0)
pl.scatter(a, b, marker='.')
pl.scatter(X, Y, c='red')
pl.axis('equal')

M=pl.matrix(M)
    
pl.figure(1)
mappa=colors.LinearSegmentedColormap.from_list('Potenziale', [(0, 'blue'), (0.5, 'white'), (1, 'red')], 256)
imm=pl.imshow(M, interpolation='nearest', cmap=mappa)
pl.colorbar(imm, cmap=mappa)

pl.show()
