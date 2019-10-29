###SECONDA BREVE LEZIONE DI PYTHON - 13 novembre 2019
#cominciamo importando le librerie
import numpy as np
import math


###ARRAY
print('\nARRAY')
#Un array unidimensionale è semplicemente una sequenza ordinata (un vettore) di numeri.

#Creiamo un array di 5 elementi
array1=np.array([1.0, 2.0, 4.0, 8.0, 16.0]) #notare che la scrittura 2. e 2.0 è equivalente

print(array1)

#per accedere a un singolo elemento dell'array basta fare come segue:
elem=array1[1]

#ATTENZIONE! Gli indici, per Python, partono da 0, non da 1!
print(elem)


#Supponiamo di voler aggiungere un altro numero, ad esempio 18, al nostro array1, e di volerlo aggiungere al quinto posto (che per Python sarà il quarto perchè parte dalla posizione 0).
# Il modo per farlo è il seguente:
array1=np.insert(array1, 4, 18) #possiamo anche non chiamarlo array1, in quel caso avremo un nuovo array uguale all'array1 ma con un numero in più
#quindi: il primo argomento è l'array a cui vogliamo aggiungere qualcosa, il secondo argomento è il posto (-1) dove vogliamo aggiungere il numero, e il terzo argomento è il numero che vogliamo aggiungere
print(array1)

##Tipi di array
#ogni array di numpy ha un tipo ben definito che viene fissato, implicitamente o esplicitamente al momento della creazione

#per sapere di che tipo è l'array si usa la funzione dtype:
tipoarray1=array1.dtype
print(tipoarray1)

#tipo definito implicitamente:
a=np.array([0, 1, 2]) #abbiamo scritto solo numeri interi => array di interi
b=np.array([0., 1., 2.]) #abbiamo scritto solo numeri con la virgola => array di numeri float
#nota: anche se si dice "numero con la virgola", vanno scritti sempre col punto! La virgola separa gli argomenti
c=np.array([0, 3.14, 'giallo']) #quest'array è misto. In genere se ci sono sia numeri interi che float che stringhe


#il tipo si può anche definire esplicitamente al momento della creazione, nelseguente modo:
d=np.array([0., 1., 2.], 'int')
e=np.array([0, 1, 2], 'float')

print(d, d.dtype)
print(e, e.dtype)

##Lunghezza di un array
lunghezza=len(e) #restituisce come valore il numero di elementi dell'array cui nome è tra le parentesi tonde

##Array predefiniti
arraydizeri=np.zeros(3)
arraydizerii=np.zeros(3, 'int')
arraydiuni=np.ones(5)
arraydiuni=np.ones(5, 'int')

##Operazioni con gli array
print('\nOperazioni con gli array:')
#Come per i vettori, si possono sommare e sottrarre vettori che abbiano la stessa dimensione, nel nostro caso array con lo stesso numero di elementi (altrimenti Python da errore!)


#Le operazioni sono eseguite elemento per elemento!

v=np.array([4, 5, 6])
w=np.array([1.2, 3.4, 5.8])

somma=v+w
sottr=v-w
molt=v*w
div=v/w

print(v, w)
print(somma, sottr, molt, div)

#altre operazioni strane
print(v**2)
print(np.log10(w))

#attenzione: le funzioni della libreria math non sono adatte ad operare su array di lunghezza superiore a 1; per fortuna tutto quello che in genere ci serve ce l'abbiamo nella libreria numpy
#print(math.log10(w))

##Esempio di utilizzo degli array: calcolo della media e deviazione standard
print('\nCalcolo media e deviazione standard')
#Nelle eseperienze di laboratorio 1 quasi sempre si ha a che fare con una serie di misure di cui poi vogliamo calcolare media e deviazione standard
#può essere comodo, soprattutto quando abbiamo tanti dati, usare gli array
misurag=np.array([9.81, 9.82, 10, 9.65, 9.807])
#come prima cosa ci serve la somma di tutte le misure e il numero totale di misure
# esiste un modo semplice per calcolare la somma di tutti gli elementi di un array, che è il seguente:
sum= misurag.sum()
#per quanto riguarda il numero di misure fatte, senza stare a contarle, abbiamo già visto che esiste una funzione che lo fa per noi, che è "len"
n=len(misurag)

media=sum/n
print('La media è %f' %media)
#in realtà c'è una funzione fatta apposta per calcolare la media, ma noi in teoria potevamo non saperlo...
media2=np.mean(misurag)

#sappiamo che la deviazione standard è la radice della varianza, e la varianza è la somma dei quadrati delle misure-la media, tutto diviso per n*(n-1)

#facciamo tutti i calcoli passo passo

#creiamo un array che abbia come elementi i quadrati di (misura i-esima - media)
vett=misurag-media
#eleviamo gli elementi al quadrato (il nome dell'array lo possiamo lasciare uguale tanto non ci servirà più e verrà sovrascritto)
vett=vett**2

#ora sommiamo tutti gli elementi del vettore
vett=vett.sum()

#dividiamo per n-1
vett=vett/((n-1)*n)


#infine:
devst=np.sqrt(vett)


#anche stavolta c'è già nella libreria di numpy la deviazione standard
devstandard=np.std(misurag)
#solo che divide sotto radice per n, non per n*(n-1) come abbiamo fatto noi

print('La deviazione standard è %f' %devst)

print('g = %.1f +- %.1f' %(media, devst) )


###MATRICI
print('MATRICI')
#c'è la funzione apposita di numpy per scrivere matrici. 
matrice1= np.matrix('1 2; 3 4; 5 6')   #Si scrivono essenzialmente i vettori riga della matrice separati da ;
#equivalente a:
matrice2=np.matrix([[1, 2], [3, 4], [5,6]])
print(matrice1)
print(matrice2)


matricedizeri=np.zeros((3, 2)) #tre righe, due colonne: matrice 3x2
print('Matrice di zeri:\n', matricedizeri, '\n')
matricediuni=np.ones((3,2))
print('Matrice di uni:\n', matricediuni, '\n')



sommadimatrici=matrice1+matricediuni
print('Somma di matrici:\n', sommadimatrici)


matrice3=np.matrix('3 4 5; 6 7 8') #matrice 2x3
prodottodimatrici=matrice1*matrice3  #matrice 3x(2x2)x3
print('\nProdotto di matrici:\n', prodottodimatrici)
