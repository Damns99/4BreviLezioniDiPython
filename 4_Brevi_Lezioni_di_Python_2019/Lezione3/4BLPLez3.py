### TERZA BREVE LEZIONE DI PYTHON - 20 novembre 2019
# Al solito, importiamo le librerie
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import pylab

# Scopo di questa lezione è quello di imparare a prelevare dati da file e produrre semplici grafici. Per farlo, avremo bisogno preliminarmente del concetto di funzione.

### FUNZIONI
print('FUNZIONI')
# Come in matematica, una funzione è essenzialmente una ricetta che a partire da un set di dati iniziali fornisce qualcosa in uscita. Un possibile esempio:
def area(a,b):
    A = a*b
    return A
# Questo è un esempio di dichiarazione di funzione che calcola l'area di un rettangolo. a e b (lati) sono gli argomenti, A (area) è la variabile restituita dalla funzione.

# 'Chiamare' una funzione vuol dire farla eseguire al computer con uno specificato set di valori iniziali. Ad esempio:
print(area(3,4))    # dovrebbe restituire 12

# Se la funzione non restituisce nulla ma esegue solo un pezzo di codice, si parla più propriamente di procedura e il valore restituito è None.
def procedura(a):
    a = a+1
print(procedura(2)) # dovrebbe restituire 3
# Volendo si possono creare anche funzioni che non hanno valori in ingresso:
def pigreco():
    return 3.14
print(pigreco())

# Bisogna notare due cose importanti:
# 1) E' fondamentale in Python che il corpo della funzione sia indentato!
# 2) Definendo degli argomenti per una funzione si creano delle variabili 'locali', il cui nome non influenza tutto quello che c'è fuori dalla funzione stessa. Ad esempio, per la funzione area abbiamo definito una variabile b, ma posso tranquillamente definire una nuova variabile b al di fuori della funzione.

# Definire una funzione può essere comodo per ripetere agevolmente pezzi di codice. Infatti, tutte le volte che utilizziamo librerie stiamo di fatto chiamando delle funzioni in esse definite. Librerie = pacchetti di funzioni.



### INPUT DA FILE
print('\nINPUT DA FILE')
# Supponiamo di avere un file da cui vogliamo estrarre dei dati e supponiamo che i singoli numeri siano separati da tabulazioni e andate a capo.

dati = np.loadtxt('dati-lezione.txt')
print(dati)
# Tale istruzione crea una "matrice" dati in cui inserisce i dati così come riportati nel file. Può essere più comodo creare array diversi per ogni riga:
dati1, dati2, dati3 = np.loadtxt('dati-lezione.txt')
print(dati1, dati2, dati3)

# Equivalentemente può essere utilizzata l'istruzione pylab.loadtxt invece di np.loadtxt. Se volessimo raggruppare i dati in colonne piuttosto che in righe (come solitamente è) basta scrivere:
dati1, dati2 = np.loadtxt('dati-lezione.txt', unpack = True)
print(dati1,dati2)
# In questo modo gli array dati1 e dati2 contengono, rispettivamente, la prima e la seconda colonna di dati.

# Esistono metodi diversi e più elaborati per trattare file che possiedono una struttura diversa, ma per quanto riguarda l'utilizzo che se ne fa in laboratorio questo modo di fare è sufficiente. Se siete interessati a tale tematica, possiamo studiare delle tecniche insieme!


### GRAFICI

## Grafici di funzioni

plt.figure(1)

# Per creare un grafico bidimensionale abbiamo bisogno di due set di dati, rispettivamente per le ascisse e per le ordinate. Supponiamo, per iniziare, di voler stampare il grafico della funzione f(x) = x**3 nel range [-1,1]. La funzione è definita da:
def f(x):
    return x**3
# mentre per creare un array di numeri equispaziati nel range [-1,1] usiamo:
x = np.linspace(-1, 1, 1000)
# Il primo argomento è l'inizio della sequenza, il secondo è la fine (inclusa) e il terzo indica il numero di punti creati.

plt.plot(x, f(x))   # crea il grafico
plt.show()          # lo stampa a video

# Sono possibili numerose opzioni per modificare l'aspetto e la formattazione di un grafico. Molte sono disponibili nell'apposita schermata fornita a video dal pacchetto matplotlib. Vediamo come effettuare queste modifiche direttamente tramite codice Python.

plt.axis([-1.1, 1.1, -1.1, 1.1])
# Imposta, rispettivamente, il minimo e il massimo delle x e il minimo e il massimo delle y

plt.yticks([-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0])
# Inserisce manualmente i tick dell'asse y

plt.title('Il mio primo grafico')
# Imposta il titolo del grafico

plt.xlabel('$x$', fontsize = 20)
plt.ylabel('$x^3$', fontsize = 20)
# Impostano le etichette degli assi. All'interno degli apici si possono scrivere anche caratteri in stile LaTeX, infatti l'utilizzo di $..$ sta proprio ad indicare lo stile matematico di scrittura. Ad esempio per scrivere la lettera greca alpha è sufficiente inserire $\alpha$.

plt.grid()
# Inserisce un griglia

# E se volessi inserire più curve nello stesso plot?
def g(x):
    return x**2
plt.plot(x, g(x))
# Per distinguerle è possibile formattare molto liberamente colore, stile della linea e tanto altro. Ad esempio:
plt.plot(x, g(x), color = 'red', linestyle = '--')
# disegna una linea rosso tratteggiata. Per altre opzioni consultare il manuale di matplotlib o modificare direttamente le impostazioni nell'apposita sezione mostrata a video quando si stampa il grafico.

# Per mostrare una legenda è necessario dotare le singole curve di un'etichetta, ad esempio:
plt.plot(x, f(x), label = 'Prima funzione')
plt.plot(x, g(x), label = 'Seconda funzione')
plt.legend()
# La funzione legend è dotata di numerosissimi argomenti opzionali, quali la regolazione della dimensione, della posizione ecc. Ad esempio:
plt.legend(loc = 'best', fontsize = 15)
# posizione la legenda nel posto (secondo lui) migliore con dimensione 15pt per i caratteri al suo interno.

## Grafici in scala logaritmica

# Con il seguente comando creiamo una nuova finestra grafica
plt.figure(2)

# In questo esempio facciamo uso di un array fatto di elementi linearmente equispaziati:
x = np.linspace(0,10,1000)
# In generale, potremmo anche aver bisogno di un array fatto di elementi logaritmicamente equispaziati. In tal caso si usa la funzione:
z = np.logspace(0,2,1000,base = 10.0)
# I primi due argomenti indicano che la sequenza comincia da 10^0 e finisce con 10^2 (inclusi). Il terzo argomento, al solito, indica di quanti punti è fatta la sequenza e l'ultimo argomento indica la base logaritmica.

def h(x):
    return np.exp(2*x)
plt.plot(x, h(x))
plt.grid()

# Con il seguente comando impostiamo la scala logaritmica sull'asse y
plt.yscale('log')
# Volendo, può essere fatto analogamente per l'asse x

plt.show()

# Con il comando plt.close(1), volendo, possiamo chiudere la prima finestra. Con plt.close('all') si chiudono tutte le finestre grafiche aperte fino a quel momento.


## Grafici di punti e istogrammi

plt.figure(3)
# Passiamo adesso al plotting di set di dati acquisiti da file.
# Consideriamo come esempio l'esperienza in cui dovrete misurare l'accelerazione di gravità tramite una molla. Abbiamo vari pesetti da poggiare su un piattello attaccato ad una molla in posizione verticale. Dalla seconda legge della dinamica, sappiamo che, all'ordine più basso, esiste una relazione lineare tra massa e allungamento della molla:
# l = (g/k)m + l_0
# dove k è la costante elastica ed l_0 è la lunghezza a riposo.
# Supponiamo di aver scritto un file le cui colonne di dati rappresentano, nell'ordine: massa, errore sulla massa, allungamento, errore sull'allungamento.
# Innanzitutto abbiamo bisogno di importare nel programma tali informazioni:
m, dm, l, dl = np.loadtxt('dati.txt', unpack = True)

# Il seguente comando raffigura i singoli punti, collegandoli:
plt.errorbar(m, l, dl, dm)
# Da notare l'ordine degli argomenti della funzione!

# Come prima, esistono numerosi argomenti aggiuntivi in grado di formattare lo stile e il colore del grafico. Ad esempio:
plt.errorbar(m, l, dl, dm, linestyle = '', marker = 'o', color = 'red')
# rende i punti dei pallini rossi e cancella la linea che li collega

# Per fare qualche belluria:
plt.xlabel('Massa [g]')
plt.ylabel('Allungamento [cm]')
plt.title('Allungamento di una molla verticale')
plt.grid()
plt.show()

# Tramite la determinazione del coefficiente angolare della "retta che meglio collega tali punti" è possibile ricavare g (conoscendo k). Vedremo la prossima settimana come effettuare procedure di best-fit atte proprio a risolvere problemi di questo tipo.


plt.figure(4)
# Per concludere, vediamo un comando che permette di realizzare un semplice istogramma.
# Sull'asse x utilizziamo un array di 10 punti equispaziati.
x = np.linspace(1,10,10)
# Sull'asse y abbiamo, ad esempio, il seguente set di dati:
y = np.array([2.54, 4.78, 1.13, 3.68, 5.79, 7.80, 5.4, 3.7, 9.0, 6.6])

# Il comando per la creazione dell'istogramma corrispondente è:
plt.bar(x, y, align = 'center')

plt.figure(5)
z=np.random.random(10)*10
plt.hist(z,[0,2,4,6,8,10],rwidth=0.9)
# dove l'argomento aggiuntivo serve a centrare le barre con i numeri sull'asse x.

# Un po' di bellurie...
plt.xticks(np.linspace(0,12,13))

plt.show()