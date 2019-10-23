import pylab
import numpy
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox

test=1

def sign_to_c(x,c):
    i=0
    while(10**c>x):
        x=x*10
        i=i+1
    while(10**c<x):
        x=x/10
        i=i-1
    return i

nomefile='f_'+str(test)+'.txt'
percorso='./'+nomefile

def fit_function(x,th0,tau):
    return th0*numpy.e**(-x/tau)
    
def inv_func(y,th0,tau):
    return -tau*numpy.log(y/th0)

# Load the data from the file. i t sono i quadrati
ta, sa, tb, sb = pylab.loadtxt(percorso, unpack = True)
msa=numpy.mean(sa)
msb=numpy.mean(sb)
sa-=msa
sb-=msb

if(test>=4):
    sa=sb
    ta=tb

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

pylab.minorticks_on()
pylab.grid(color = 'gray', which = 'major') 
pylab.grid(color = 'gray', which = 'minor', alpha=0.1)
pylab.xlabel("tempo [s]")
pylab.ylabel("ampiezza [u.a.]")
pylab.title(nomefile)
l,=pylab.plot(ta,sa,color='orange', linewidth=0.5)
D,=pylab.plot(ta,sa,color='red', linewidth=0.8)
Merr,qqq,qqq=pylab.errorbar(ta,sa,linestyle = '', color = 'red', marker='.')
merr,qqq,qqq=pylab.errorbar(ta,sa,linestyle = '', color = 'red', marker='.')
w0=1.0
dw0=0.01
cif=str(sign_to_c(dw0,2))
formtw="%."+cif+"f +- %."+cif+"f"
dec=1.0
errdec=0.01
cif=str(sign_to_c(errdec,2))
formta="%."+cif+"f +- %."+cif+"f"
omegaax=plt.axes([0.1, 0.09, 0.15, 0.075])
omega=TextBox(omegaax, 'w ', initial=formtw)
ampiezzaax=plt.axes([0.1, 0.015, 0.15, 0.075])
ampiezza=TextBox(ampiezzaax, 't_dec ', initial=formta)

massimot=0.8*numpy.array(ta).max()

##
def Ripeti(sa,ta):
    global dec, errdec, dw0, w0, massimot
    max=[0. for r in range(100)]
    maxt=[0. for r in range(100)]
    c=0
    for i in range(1,sa.size-3):
        if(sa[i]>sa[i-1] and sa[i]>=sa[i+1] and sa[i]>=sa[i+2] and sa[i]>sa[i-2] and sa[i]>sa[i-3] and sa[i]>sa[i+3] and ta[i]<=massimot):
            max[c]=(sa[i])
            maxt[c]=(ta[i])
            c+=1
    d=c
    while(d<100):
        max.remove(0.)
        maxt.remove(0.)
        d+=1
    Merr.set_data(maxt,max)
        
    min=[0. for r in range(100)]
    mint=[0. for r in range(100)]
    cc=0
    for i in range(1,sa.size-3):
        if(sa[i]<sa[i-1] and sa[i]<=sa[i+1] and sa[i]<=sa[i+2] and sa[i]<sa[i-2] and sa[i]<sa[i-3] and sa[i]<sa[i+3] and ta[i]<=massimot):
            min[cc]=(sa[i])
            mint[cc]=(ta[i])
            cc+=1
    d=cc
    while(d<100):
        min.remove(0.)
        mint.remove(0.)
        d+=1
    merr.set_data(mint,min)
        
    d=0
    diff=[0. for r in range(c)]
    for i in range(1,c):
        diff[d]=maxt[i]-maxt[i-1]
        d+=1
    
    T=numpy.mean(diff[0:d])
    dT=0.0
    dT=numpy.std(diff[0:d])
    dT/=numpy.sqrt(d-1)
    
    w0=2*numpy.pi/T
    dw0=w0*dT/T
    
    print("T = %.4f +- %.4f" %(T, dT))
    print("w_0 = %.4f +- %.4f" %(w0,dw0))
    
    cif=str(sign_to_c(dw0,2))
    formt="%."+cif+"f +- %."+cif+"f"
    omega.set_val(formt %(w0, dw0))
    
    a=numpy.sqrt(9.81*0.506/(0.5*0.0475**2+0.506**2))
    da=0.5/a*9.81*((0.506/(0.5*0.0475**2+0.506**2))*(0.005/0.506+((0.0005+2*0.005)/(0.5*0.0475**2+0.506**2))))
    print("w_t = %.4f +- %.4f" %(a,da))
    print("scarto = %.4f" %(w0-a))
        
    A=numpy.asarray([T,dT])
    
    cerca=max[3]/numpy.e
    print("valore cercato = %.4f" %cerca)
    
    dec=0
    for i in range(1,numpy.minimum(c-1, cc-1)):
        if(max[i]>=cerca and (-min[i+1])<=cerca):
            dec=(maxt[i]+mint[i+1]-2*maxt[3])/2
            errdec=(mint[i+1]-maxt[i])/2
            print("tau_d = %.4f +- %.4f\n" %(dec,errdec))
            cif=str(sign_to_c(errdec,2))
            formt="%."+cif+"f +- %."+cif+"f"
            ampiezza.set_val(formt %(dec, errdec))
        elif(-min[i]>=cerca and max[i+1]<=cerca):
            dec=(mint[i]+maxt[i+1]-2*maxt[3])/2
            errdec=(maxt[i+1]-mint[i])/2
            print("tau_d = %.4f +- %.4f\n" %(dec,errdec))
            cif=str(sign_to_c(errdec,2))
            formt="%."+cif+"f +- %."+cif+"f"
            ampiezza.set_val(formt %(dec, errdec))
    
##

axbox1=plt.axes([0.41, 0.05, 0.1, 0.075])
text_box1=TextBox(axbox1, 'xmin', initial='0.0')
axbox2=plt.axes([0.61, 0.05, 0.1, 0.075])
text_box2=TextBox(axbox2, 'xmax', initial='100.0')

def onsubmitted1(min):
    global massimot
    if(eval(min)>=eval(text_box2.text)):
        xmin=eval(text_box2.text)-1.
    else:
        xmin=eval(min)
    indmin, indmax = numpy.searchsorted(numpy.array(ta), (xmin,eval(text_box2.text)))
    thisx = ta[indmin:indmax]
    thisy = sa[indmin:indmax]
    D.set_data(thisx, thisy)
    massimot=1*numpy.array(thisx).max()
    Ripeti(thisy,thisx)
    fig.canvas.draw()
    plt.draw()

text_box1.on_submit(onsubmitted1)

def onsubmitted2(max):
    global massimot
    if(eval(max)<=eval(text_box1.text)):
        xmax=eval(text_box1.text)+1.
    else:
        xmax=eval(max)
    indmin, indmax = numpy.searchsorted(numpy.array(ta), (eval(text_box1.text),xmax))
    thisx = ta[indmin:indmax]
    thisy = sa[indmin:indmax]
    D.set_data(thisx, thisy)
    massimot=1*numpy.array(thisx).max()
    Ripeti(thisy,thisx)
    fig.canvas.draw()
    plt.draw()

text_box2.on_submit(onsubmitted2)

def onselected(xmin, xmax):
    if(xmin>xmax):
        tmp=xmin
        xmin=xmax
        xmax=tmp
    text_box1.set_val(int(xmin*100.)/100.)
    text_box2.set_val(int(xmax*100.)/100.)
    indmin, indmax = numpy.searchsorted(numpy.array(ta), (xmin, xmax))
    thisx = ta[indmin:indmax]
    thisy = sa[indmin:indmax]
    D.set_data(thisx, thisy)
    massimot=1*numpy.array(thisx).max()
    Ripeti(thisy,thisx)
    fig.canvas.draw()
    plt.draw()

span = SpanSelector(ax, onselected, 'horizontal', useblit=True, rectprops=dict(alpha=0.5, facecolor='red'))

def onclicked1(val):
    text_box1.set_val(int(min(ta)*100.)/100.)
    text_box2.set_val(int(max(ta)*100.)/100.)
    thisx = ta
    thisy = sa
    D.set_data(thisx, thisy)
    massimot=0.8*numpy.array(ta).max()
    Ripeti(thisy,thisx)

axbutt=plt.axes([0.76, 0.05, 0.1, 0.075])
bbutt=Button(axbutt, 'Reset')
bbutt.on_clicked(onclicked1)

def onclicked2(val):
    cif=sign_to_c(dw0,2)
    w0conv=numpy.rint(w0*(10**cif))/(10.**cif)
    dw0conv=numpy.rint(dw0*(10**cif))/(10.**cif)
    cif=sign_to_c(errdec,2)
    decconv=numpy.rint(dec*(10**cif))/(10.**cif)
    errdecconv=numpy.rint(errdec*(10**cif))/(10.**cif)
    A=numpy.asarray([test,decconv,errdecconv,w0conv,dw0conv])
    with open("vediamo.txt", 'a') as f:
        numpy.savetxt(f, A.reshape(1,5), delimiter='\t', newline='\r\n', fmt='%s')

axbutt2=plt.axes([0.87, 0.05, 0.1, 0.075])
bbutt2=Button(axbutt2, 'Salva')
bbutt2.on_clicked(onclicked2)

def sx(val):
    global test, nomefile, ta, sa, tb, sb, massimot
    if(test>1):
        test-=1
        
        nomefile='f_'+str(test)+'.txt'
        percorso='./'+nomefile
        ax.set_title(nomefile)
        ta, sa, tb, sb = pylab.loadtxt(percorso, unpack = True)
        msa=numpy.mean(sa)
        msb=numpy.mean(sb)
        sa-=msa
        sb-=msb
        
        if(test>=4):
            sa=sb
            ta=tb
        
        l.set_data(ta,sa)
        massimot=0.8*numpy.array(ta).max()
        onclicked1(0)
        xlen=max(ta)-min(ta)
        ylen=max(sa)-min(sa)
        xmin=min(ta)-0.1*xlen
        xmax=max(ta)+0.1*xlen
        ymin=min(sa)-0.1*ylen
        ymax=max(sa)+0.1*ylen
        ax.set_xlim(left=xmin, right=xmax)
        ax.set_ylim(top=ymax, bottom=ymin)

axbuttsx=plt.axes([0.02, 0.49, 0.05, 0.2])
bbuttsx=Button(axbuttsx, '<')
bbuttsx.on_clicked(sx)

def dx(val):
    global test, nomefile, ta, sa, tb, sb, massimot
    if(test<6):
        test+=1
        
        nomefile='f_'+str(test)+'.txt'
        percorso='./'+nomefile
        ax.set_title(nomefile)
        ta, sa, tb, sb = pylab.loadtxt(percorso, unpack = True)
        msa=numpy.mean(sa)
        msb=numpy.mean(sb)
        sa-=msa
        sb-=msb
        
        if(test>=4):
            sa=sb
            ta=tb
        
        l.set_data(ta,sa)
        massimot=0.8*numpy.array(ta).max()
        onclicked1(0)
        xlen=max(ta)-min(ta)
        ylen=max(sa)-min(sa)
        xmin=min(ta)-0.1*xlen
        xmax=max(ta)+0.1*xlen
        ymin=min(sa)-0.1*ylen
        ymax=max(sa)+0.1*ylen
        ax.set_xlim(left=xmin, right=xmax)
        ax.set_ylim(top=ymax, bottom=ymin)

axbuttdx=plt.axes([0.93, 0.49, 0.05, 0.2])
bbuttdx=Button(axbuttdx, '>')
bbuttdx.on_clicked(dx)

Ripeti(sa,ta)

pylab.show()