#Cigottero Marco 5 a rob

import math
import numpy as np

def encode(mes, c, n):  #codifico il messaggio
    return ((mes**c)%n)

def decode(mess, d, n):  #decodifico il messaggio
    return ((mess**d)%n)

def isPrime(n): #verifico se il nuemero inserito è primo

    for p in range(2, int(np.sqrt(n)) + 1):
        if (n % p == 0):
            return False
    return True


def mcd(a, b):  #calcolo l'mcd
    while True:
        r = a % b   #calcolo il resto
        if r == 0:  #se r è uguale a zero vuol dire che b è un divisore di a
            break   #quindi esco perchè ho trovato il divisore più alto comune

        a, b = b, r

    return b

while True:
    print("Inserire p:")    #inserisco p e q
    p = int(input())
    print("inserire q:")
    q = int(input())
    if isPrime(p):      #controllo che siano primi
        if isPrime(q):
            break
        else:
            print("numero q non primo riprovare")
    else:
        print("numero p non primo riprovare")



n = int(p * q)          #calcolo n

m = 0
if(p>q):    #scelgo il maggiore tra p e q
    maggiore = p
else:
    maggiore = q
while(m==0):
    if((maggiore % (p-1) == 0) and (maggiore % (q-1) == 0)):    #cerco l'mcm
        m = maggiore                                            #assegno a m
        break
    maggiore = maggiore + 1
#print("m =", m)

#cerco c
for i in range (2, m):  #cerco il numero tra 1 e m
        if mcd(i, m) == 1:  #condizione per la quale c sia valido
            break
c=i
#print("c=", c)

d = 0
while(True):
    if((c*d)%m == 1):   #cerco d con il metodo della brute force
        break
    else:
        d = d + 1

#print("d =", d)

print("Chiave pubblica: n=", n," c=", c)    #divulgo le chiavi pubbliche
# print("Chiave privata: m=", m," d=", d) tengo segrete le chiavi private

messaggio=10
print(f"Messaggio da decodificare e inviare  {messaggio}")
messaggio_codificato = encode(messaggio, c, n)
print(f"Messaggio codificato = {messaggio_codificato}")