import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig=plt.figure()
ax=fig.add_subplot(111)
nomeinput='Disegno.png'
ax.set_title(nomeinput)
img=mpimg.imread(nomeinput)
imgplot=plt.imshow(img, clim=(0,1))
numsave=0

punti=[0 for i in range(1000)]
index=0
dragx=0.
dragy=0.
cliccato=False

def updrag(event):
    global dragx
    global dragy
    global cliccato
    dragx=event.xdata
    dragy=event.ydata
    cliccato=True

def salva():
    global punti
    global index
    global nomeinput
    global numsave
    global ax
    for i in range(index):
        xi=punti[i].lines[0].get_data()[0][0]
        yi=punti[i].lines[0].get_data()[1][0]
        A=np.asarray([xi,yi])
        nomeoutput=nomeinput+str(numsave)+'_o.txt'
        with open(nomeoutput, 'a') as f:
            np.savetxt(f, A.reshape(1,2), delimiter='\t', newline='\r\n', fmt='%.4f')
    numsave+=1
    ax.set_ylabel(str(numsave))
    fig.canvas.flush_events()
    fig.canvas.draw()
    print("XYdata Saved")
    return

def onclick(event):
    global punti
    global index
    global dragx
    global dragy
    global ax
    if(event.button==2 or (event.key=='shift' and event.button==1)):
        salva()
        return
    if(event.key=='shift' and event.button==3):
        reset()
        return
    if((dragx-event.xdata)**2>64. or (dragy-event.ydata)**2>64. or index>=1000):
        print(dragx,event.xdata)
        return
    if(event.button==1):
        newx=event.xdata
        newy=event.ydata
        punti[index]=plt.errorbar(newx,newy,color='red',marker='.')
        index+=1
        print("Point Created")
        print("%d total points" %index)
        ax.set_xlabel(str(index))
        fig.canvas.draw()
    elif(event.button==3):
        for i in range(index):
            xi=punti[i].lines[0].get_data()[0][0]
            yi=punti[i].lines[0].get_data()[1][0]
            gomma=5.
            if(event.key=='control'):
                gomma=50.
            if(event.xdata>=xi-gomma and event.xdata<=xi+gomma and event.ydata>=yi-gomma and event.ydata<=yi+gomma):
                punti[i].lines[0].remove()
                punti.pop(i)
                index-=1
                print("Point Deleted")
                print("%d total points" %index)
                ax.set_xlabel(str(index))
                fig.canvas.flush_events()
                fig.canvas.draw()
                return
                
def onclickplus(event):
    global cliccato
    onclick(event)
    cliccato=False
    return

def ondrag(event):
    global dragx
    global dragy
    global cliccato
    if(not(cliccato)):
        return
    if(((dragx-event.xdata)**2<64. and (dragy-event.ydata)**2<64.) or index>=1000):
        return
    dragx=event.xdata
    dragy=event.ydata
    onclick(event)
    return

def reset():
    global punti
    global index
    global dragx
    global dragy
    global ax
    for i in range(index):
        punti[i].lines[0].remove()
    index=0
    ax.set_xlabel(str(index))
    fig.canvas.flush_events()
    fig.canvas.draw()
    punti=[0 for i in range(100)]
    dragx=0.
    dragy=0.
    print("Reset Completed")
    return
                
connid = fig.canvas.mpl_connect('button_release_event', onclickplus)
connid = fig.canvas.mpl_connect('button_press_event', updrag)
connid = fig.canvas.mpl_connect('motion_notify_event', ondrag)

plt.show()