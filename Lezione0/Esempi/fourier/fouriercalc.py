import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.image as mpimg

fig, ax=plt.subplots()
ax.axis('equal')
re, im=np.loadtxt('Disegno.png0_o.txt',unpack=True)
mre=re.mean()
mim=im.mean()
re-=mre
im-=mim

nomeinput='Disegno.png'
#ax.set_title(nomeinput)
img=mpimg.imread(nomeinput)
imgplot=plt.imshow(img, clim=(0,1), alpha=0.5)

nv=int(len(re)/2)
for c in range(-nv,nv+1):
    sr=0.
    si=0.
    for i in range(len(re)):
        er=np.cos(-c*2*np.pi*i/len(re))
        ei=np.sin(-c*2*np.pi*i/len(re))
        sr+=re[i]*er-im[i]*ei*1./len(re)
        si+=re[i]*ei+im[i]*er*1./len(re)
    A=np.asarray([sr,si])
    with open('c_o.txt', 'a') as f:
        np.savetxt(f, A.reshape(1,2), delimiter='\t', newline='\r\n', fmt='%.4f')

cr, ci=np.loadtxt('c_o.txt',unpack=True)        
x=[]
y=[]
totp=1000
for i in range(totp):
    t=i/float(totp)
    xx=0.
    yy=0.
    for c in range(-nv,nv+1):
        er=np.cos(c*2*np.pi*t)
        ei=np.sin(c*2*np.pi*t)
        xx+=cr[c+nv]*er-ci[c+nv]*ei
        yy+=cr[c+nv]*ei+ci[c+nv]*er
    x.append(xx)
    y.append(yy)

x=np.array(x)
y=np.array(y)
x=x
x=x/len(re)
y=-y
x+=mre
y-=mim

#ax.plot(x,-y)
#ax.errorbar(re,-im,marker='.',linestyle='')
mat, = ax.plot(x,-y,color='red')
def animate(j):
    global x, y, totp
    dist=200
    if(j>dist-1 and j<totp-dist):
        a=x[(totp+j-dist)%totp:(totp+j+dist)%totp]
        b=y[(totp+j-dist)%totp:(totp+j+dist)%totp]
    else:
        a=x[(totp+j-dist)%totp:totp]
        a=np.append(a,x[0:(totp+j+dist)%totp])
        b=y[(totp+j-dist)%totp:totp]
        b=np.append(b,y[0:(totp+j+dist)%totp])
    mat.set_data(a,-b)
    return mat,
ani = animation.FuncAnimation(fig, animate, frames=totp, interval=5, blit=True, repeat=True, repeat_delay=0)
plt.show()