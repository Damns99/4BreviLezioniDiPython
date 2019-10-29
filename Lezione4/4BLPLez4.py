### TERZA BREVE LEZIONE DI PYTHON - 27 novembre 2019
import numpy as np
import pylab
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

##BEST FIT
#Come prima cosa, carichiamo il nostro set di dati dal file datilez4.txt
x, Dx, y, Dy = pylab.loadtxt('dati-lezione4.txt', unpack=True)

#Prima di eseguire la procedura di best-fit, è necessario osservare l'andamento di tali dati, che potrebbe essere lineare, quadratico, etc..
#Quindi, per prima cosa, stampiamo il grafico riportando solo le misure e i relativi errori.
#Ciò che sta sugli assi va sempre specificato, insieme alla sua unità di misura
#In genere le grandezze si scrivono in corsivo, cioè tra i $$, e le unità di misura tra parentesi quadre

plt.figure(1)
plt.title('Misure di corrente e tensione', fontsize=16)
plt.xlabel('$\Delta V$ [V]')
plt.ylabel('$I$ [mA]')
plt.errorbar(x, y, Dy, Dx, linestyle='', color='black', marker='.')
plt.grid()
plt.show()

#Una volta appurato l'andamento dei dati, nel nostro caso lineare, procediamo con la definizione della funzione con cui vogliamo eseguire il fit.
#Essendo l'andamento lineare, la funzione cercata sarà una retta.

#Nella scorsa lezione abbiamo visto come si creano prototipi di funzioni.

#Per una retta generica, abbiamo bisogno di assegnare 3 argomenti alla funzione: la variabile indipendente x, il coefficiente angolare m, e l'intercetta q

def funzionefit(x, m, q):
    return m*x + q
    
#Python possiede un algoritmo che cerca per noi la migliore funzione possibile che interpola i nostri dati. Ha bisogno però di alcune informazioni oltre ai dati stessi, ovvero i valori iniziali. 
#La funzione curve_fit utilizza un metodo numerico iterativo per la stima dei parametri: si parte dai valori iniziali che forniamo noi e li fa variare in modo opportuno fino a che l'algoritmo non converge al minimo del χ2.
#ATTENZIONE: non è garantito che il χ2 abbia un solo minimo al variare dei parametri. In tal caso, l'assegnazione dei valori iniziali dei parametri è fondamentale perchè valori iniziali diversi per i parametri possono far convergere il fit a soluzioni diverse.
#Ciò che accade, tecnicamente, è che, quando il χ2 , in funzione dei parametri, ha più di un minimo, le procedure di fit iterative possono convergere, a seconda della scelta dei valori iniziali, ad uno dei minimi locali, anziché il minimo globale cercato.

#Dal grafico si evince che i parametri iniziali sono più o meno i seguenti (li scriviamo nell'ordine con cui sono stati scritti nella definizione di funzionefit:
init=(0.002, 0.)


#A questo punto, possiamo procedere con la funzione di fit.

#Il modo è il seguente:
pars, covm = curve_fit(funzionefit, x, y, init, Dy) 
#La funzione curve_fit richiede come argomenti, in ordine: la funzione di fit, l'array di valori della variabile indipendente x, l'array di valori della variabile dipendente y, i valori iniziali dei parametri, l'array degli errori sulla variabile y.
#Tale funzione ritorna, come valori, in ordine: l'array dei valori di best fit dei parametri e la matrice di covarianza tra i parametri.

#La matrice di covarianza è una matrice simmetrica che rappresenta la variazione di ogni variabile rispetto alle altre (inclusa se stessa).
#L'elemento i-esimo sulla diagonale è la varianza del carattere i-esimo ed è quindi sempre un valore non negativo. Ogni elemento ij della matrice è la covarianza tra i caratteri i e j. Nel caso in cui questo valore sia positivo, significa che al crescere di un carattere, cresce anche l'altro. Nel caso in cui questo valore sia negativo, accade il contrario. Se i caratteri sono statisticamente indipendenti, questo valore è 0.

print('Parametri iniziali:\n', pars)
print('Matrice di covarianza:\n', covm)

m, q=pars
dm, dq=np.sqrt(covm.diagonal())

print('\nCoefficiente angolare: %f +- %f' %(m, dm))
print('Intercetta: %f +- %f' %(q, dq))

##χ2

chisq=(((y-funzionefit(x, m, q))/Dy)**2).sum()

#Per calcolare il chi quadro ridotto, dobbiamo dividere per il numero di gradi di libertà, ovvero il numero di misure meno il numero dei "vincoli" che nel nostro caso sono m e q (2)

ndof= len(x) - len(init)

chirid= chisq/ndof

print('\nChiquadro/gdl = %f/%d = %f' %(chisq, ndof, chirid))

##Residui
#I residui non sono altro che la differenza tra la y misurata e la y del modello 
res=y - funzionefit(x, m, q)

#si possono anche normalizzare con l'errore di y
resnorm=res/Dy


##GRAFICO DEL FIT E DEI RESIDUI
#Può essere comodo graficare il fit e i residui in un unico grafico.
plt.figure(1)
plt.subplot(211) #211 significa che divido il grafico in 2 righe e 1 colonna e posiziona il grafico che stiamo per fare per 1°
plt.errorbar(x, y, Dy, Dx, linestyle='', color='black', marker='.')
plt.ylabel('$I$ [mA]')
plt.title('Best-fit')
plt.grid()
#Come visto nella lezione precedente, per disegnare una curva è conveniente creare un array ausiliario. Nel caso di una retta non è necessario, mentre nel caso di curve un po' più "curve" potrebbe esserlo.
xx = np.linspace(min(x), max(x), 100)
pylab.plot(xx, funzionefit(xx, m, q), color='red')


plt.subplot(212)
plt.title('Residui normalizzati')
pylab.xlabel('$\Delta V$ [V]') #Il nome all'asse x possiamo metterlo una volta sola se i due grafici differiscono solo per la quantità sulle y
pylab.ylabel('Res. norm [a.u]')
pylab.errorbar(x, resnorm, None, None, linestyle='--', color='blue', marker='o')
pylab.grid()
pylab.show()



### ISTRUZIONI DI CONTROLLO
print('\nISTRUZIONI DI CONTROLLO')
#Prima di poter passare alla rimozione di eventuali outliers, dobbiamo imparare le istruzioni di controllo if e for.

# Per istruzioni di controllo si intendono dei comandi che modificano il flusso di compilazione di un programma in base a determinati confronti e/o controlli su certe variabili. La teoria a riguardo è abbastanza ampia e la vedrete durante il corso di informatica. Qui ci limitiamo a illustrare due istruzioni che ci serviranno in futuro.

## Espressioni condizionali: if
# Supponiamo di voler scrivere una funzione in grado di restituire il valore assoluto di un numero.
# Una possibile soluzione è la seguente:
def assoluto(x):
    if x >= 0:          
        return x
    else:
        return -x

print(assoluto(3))
print(assoluto(-3))
# Tramite l'istruzione if effettuiamo un confronto/controllo. Se il risultato è vero (i.e. 1) il programma esegue la porzione di codice immediatamente sotto-indentata. In caso contrario, l'istruzione else prende il controllo e il programma esegue la porzione di codice indentata sotto quest'ultima. Se l'istruzione else non è presente e il controllo avvenuto con l'if risultasse falso, il programma semplicemente non fa niente.
# Vediamo un altro esempio: una funzione in grado di capire se un numero è positivo, negativo o nullo:
def segno(x):
    if x > 0:
        return 'Positivo'
    elif x == 0: 
        return 'Nullo'
    else:
        return 'Negativo'

print(segno(5))
print(segno(0))
print(segno(-4))
# Da notare che è possibile aggiungere delle coppie if/else in cascata tramite il comando "elif", che è identico semanticamente a "else if".
# Da notare anche il fatto che x == 0 è completamente diverso rispetto a x = 0, come comando!
# Il primo è un confronto tra due variabili, mentre il secondo è un'assegnazione!

## Cicli: for
# Per ciclo si intende una porzione di codice che il programma è tenuto a ripetere fin quando una certa condizione non viene verificata. Esistono vari modi per fare una cosa di questo tipo, ma quella che utilizzeremo noi sarà l'istruzione for, la quale si usa nel momento in cui il numero di ripetizioni è ben definito.
# Vediamo come esempio la scrittura di una funzione che calcola il fattoriale di un numero:

def fattoriale(n):
    R = 1
    for i in range(1, n+1):
        R = R*i
    return R
    
print(fattoriale(4))
# La variabile ausiliaria i è utilizzata in questo contesto come contatore, cioè come variabile che tiene il conto del numero di cicli effettuati. Nel caso in esame, stiamo dicendo tramite l'istruzione for che la variabile i deve variare all'interno della lista range(1, n+1) = [1,2,..., n]. Il programma effettua l'operazione R = R*i per tutti i valori possibili che i assume in questa lista, nell'ordine.

###OUTLIERS
#Outlier è un termine utilizzato in statistica per definire, in un insieme di osservazioni, un valore chiaramente distante dalle altre osservazioni disponibili.

#Nella maggioranza dei grandi campioni, alcuni dati saranno più lontani dalla media del campione di quanto sarebbe logico aspettarsi. Ciò può essere dovuto ad un errore sistematico che si è verificato nella raccolta dei dati, oppure a una fallacia nella teoria che ha orientato l'assunzione di una data distribuzione campionaria di probabilità, ma potrebbe anche essere semplicemente dovuto al caso, che ha fatto sì che nella raccolta dei dati alcune osservazioni abbiano prodotto dati molto lontani dai valori medi del campione. Inoltre, gli outliers potrebbero essere indicativi di dati errati, procedure erronee o aree sperimentali in cui alcune teorie potrebbero non essere valide. Tuttavia, un piccolo numero di dati aberranti non dovuti a condizioni anomale è dato per scontato nei grandi campioni.
x2, Dx2, y2, Dy2 = pylab.loadtxt('datiout-lezione4.txt', unpack=True)
pars2, covm2 = curve_fit(funzionefit, x2, y2, init, Dy2) 
m2, q2= pars2
plt.figure(3)
plt.title('Misure di corrente e tensione con outliers', fontsize=16)
plt.xlabel('$\Delta V$ [V]')
plt.ylabel('$I$ [mA]')
plt.errorbar(x2, y2, Dy2, Dx2, linestyle='', color='black', marker='.')
pylab.plot(xx, funzionefit(xx, m2, q2), color='red')
plt.grid()


#Ci sono chiaramente 3 punti che si discostano di molto dall'andamento previsto.
#Vogliamo quindi un nuovo array di misure senza però quelli che distano dal valore atteso dalla funzione di fit per più di 2 deviazioni standard

#dichiariamo degli array vuoti per le misure x e y e i loro errori che poi andremo a riempire con i dati che vogliamo tenere

xx2=np.array([])
yy2=np.array([])
Dxx2=np.array([])
Dyy2=np.array([])


outx=np.array([])
outy=np.array([])
Doutx=np.array([])
Douty=np.array([])

j=0
k=0
for i in range (len(x2)):
    if (np.abs(y2[i] - funzionefit(x2, m2, q2)[i])< 2*Dy2[i]): #tengo solo i dati che si discostano dalla funzione di fit per meno di 2 deviazioni standard
        xx2=np.insert(xx2, j, x2[i])
        Dxx2=np.insert(Dxx2, j, Dx2[i])
        yy2=np.insert(yy2, j, y2[i])
        Dyy2=np.insert(Dyy2, j, Dy2[i])
        j+=1
    else:
        outx=np.insert(outx, k, x2[i])
        Doutx=np.insert(Doutx, k, Dx2[i])
        outy=np.insert(outy, k, y2[i])
        Douty=np.insert(Douty, k, Dy2[i])
        k+=1

plt.figure(4)
plt.title('Misure di corrente e tensione senza outliers', fontsize=16)
plt.xlabel('$\Delta V$ [V]')
plt.ylabel('$I$ [mA]')
plt.errorbar(xx2, yy2, Dyy2, Dxx2, linestyle='', color='black', marker='.', label = 'Dati')
plt.errorbar(outx, outy, Douty, Doutx, linestyle='', color='green', marker='o', label = 'Outliers')

plt.plot(xx, funzionefit(xx, m2, q2), color='red')
plt.legend(loc = 'best', fontsize = 15)
plt.grid()
plt.show()


#A questo punto conviene rifare il fit su questo nuovo set di dati.


###FINE
