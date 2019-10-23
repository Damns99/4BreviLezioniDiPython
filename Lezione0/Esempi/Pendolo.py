import numpy as np
import matplotlib.pyplot as plt


#costanti Fisiche
g=9.81
L=2
mu=0.1 #Coefficiente di "attrito"

THETA_0=np.pi/3
THTEA_DOT_0=0


#Definizione equazione differenziale (smorzato)
def get_theta_double_dot(theta, theta_dot):
    return -mu*theta_dot-(g/L)*np.sin(theta)

#Soluzione equazione differenziale
def theta(t):
    count=0
    delta_t=0.0001
    ripeti=t/delta_t
    angolo=np.zeros(int(ripeti))
    velocita=np.zeros(int(ripeti))
    tempo=np.zeros(int(ripeti))
    theta=THETA_0
    theta_dot=THTEA_DOT_0
    for time in np.arange(0,t, delta_t):
        theta_duble_dot= get_theta_double_dot(theta, theta_dot)
        theta += theta_dot*delta_t
        theta_dot += theta_duble_dot* delta_t
        velocita[count]=theta_dot
        angolo[count]=theta
        tempo[count]=time
        count=count+1
    return theta, angolo, tempo, velocita

theta, angolo, tempo, velocita=theta(50)
plt.plot(tempo,angolo,'.',color='black')

plt.show()
