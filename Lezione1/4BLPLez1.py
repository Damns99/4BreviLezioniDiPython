###PRIMA BREVE LEZIONE DI PYTHON - 6 novembre 2019
print('Prima breve lezione di Python - 6 novembre 2019\n')



#iniziando una riga con il cancelletto, Python ignorerà automaticamente tutto ciò che segue il carattere # fino al termine della riga.

##con due o più cancelletti, in pyzo questa riga appare sottolineata (in Spyder no)


'''
è possibile commentare anche più righe
in questo modo
'''

"""
o anche
così
"""








###FUNZIONE PRINT
print('FUNZIONE PRINT:')

print('Hello world')
print('4')
#questa funzione serve a “stampare” in output il valore di una variabile o di una espressione. La useremo spesso nel corso di questo file.

#si possono anche stampare più argomenti contemporanteamente, in questa maniera:
print('Hello world', 4)
#e si può anche far andare a capo scrivendo "\n"
print('Adesso vado \n a capo')







###VARIABILI
print('\nVARIABILI')
#Per definire variabili in Python, è sufficiente utilizzare l’operatore di assegnamento (=) come nei seguenti esempi:

numerointero= 13
numeroavirgolamobile= 13.

#in Python non è necessario né definire le variabili prima di utilizzarle, né specificare il loro tipo.

#stampiamo questi numeri sulla shell
print('Numero intero:', numerointero, 'Numero a virgola mobile:', numeroavirgolamobile)

#scrivere operazioni è molto semplice
x1=3
y1=4

somma=x1+y1
prodotto=x1*y1
differenza=x1-y1
rapporto=x1/y1

print(somma, prodotto, differenza, rapporto)
#bisogna fare molta attenzione alla punteggiatura: ad esempio, se avessimo scritto la riga precedente senza virgole: 
#"print(somma prodotto differenza rapporto)", avremmo avuto sulla shell un messaggio di errore "SyntaxError: invalid syntax"


#python legge da destra verso sinistra, di conseguenza non riconosce il comando scritto così:
x1+y1=somma
print(somma)


#possiamo decidere se stampare un numero in formato di numero intero o in formato di numero con la virgola. Cerchiamo di capire meglio
a=3.14
b=6

print('%d' %a) #questo comando mi stampa il numero a come numero intero, anche se in realtà l'abbiamo definito con la virgola
print('%f' %b) #e questo comando mi stampa il numero b come numero con la virgolam anche se l'abbiamo definito come numero intero

#possiamo anche decidere quante cifre dopo la virgola stampare. Ad esempio:
c=3.141592653589793
print('%.3f' %c) #se vogliamo che il numero venga stampato con 3 cifre dopo la virgola
print('%.10f' %c) #se dopo la virgola vogliamo 10 cifre

#Achtung! A volte le cifre indicate non sono abbastanza per esprimere le giuste cifre significative

print('Volendo si possono stampare i numeri %.2f e %d anche in questo modo comodo' %(a,b))

#Attenzione ad assegnare due valori diversi ad una sola variabile: Python considererà solo quello scritto per ultimo! Vediamo un esempio:
x=30
x=18

print('x=', x) #quello che osserviamo è che Python stampa 18, e non 30. 

#E' possibile anche sovrascrivere una variabile con un numero che dipende dal suo valore precedente così:
x=x+1
#Oppure anche così:
x+=1

print('x=', x) #qui stampa 20


###LIBRERIE
print('\nLIBRERIE')
#Le librerie costituiscono un insieme di funzioni, costanti o strutture dati predefinite.
#Useremo numpy, matplotlib, math e scipy
#Prima di poter accedere ai contenuti di una libreria, è necessario importarla. Per farlo, usiamo il comando import.
#Solitamente è buona abitudine importare tutte le librerie che ci servono all'inizio del file che scriviamo
import numpy #questa libreria permette di scrivere vettori e matrici (che vedremo nelle prossime lezioni), ha al suo interno funzioni matematiche e costanti utili
#per usare un contenuto di questa libreria basta scrivere numpy.contenuto. La lista dei contenuti e dei loro nomi è disponibile online. 
pigreco=numpy.pi 
print(pigreco)

#può essere comodo anche usare un nome più breve per usare la libreria numpy. Per farlo, invece che scrivere all'inizio del nostro file "import numpy", scriviamo:
import numpy as np

pigreco=np.pi 
eulero=np.e
print(eulero)

import math #in questa libreria ci sono un sacco di funzioni matematiche utili (alcune delle quali sono contenute anche in numpy)
coseno=math.cos(0)
seno=math.sin(np.pi/2) #python usa di default gli angoli in radianti!!!
senosbagliato=math.sin(90)
print('\nCoseno di 0=', coseno, "\nSeno di pigreco mezzi=", seno, "\nSeno di 90=", senosbagliato) 
#bisogna quindi stare attenti ad avere tutti gli angoli in radianti
angoloingradi=45
angoloinradianti=math.radians(angoloingradi) #questa funzione è utile per convertire gli angoli da gradi a radianti
print("Angolo in gradi:", angoloingradi, "Angolo in radianti:", angoloinradianti)

#Spesso conviene andarsi a cercare le funzioni che ci servono, invece di provare a crearle da soli



#Nel corso delle prossime lezioni vedremo altre funzioni utili
