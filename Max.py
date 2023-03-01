Liste = [1, 21, 8, 24, 6, 58, 5, 45, 84, 35]

maxListe = Liste[0]
for k in range(1, len(Liste)):
    if Liste[k] > maxListe:
        maxListe = Liste[k]
#print("Le max de la liste est " + str(maxListe))

############################

0o11100000 & 0o00100000 == 0o00100000

############################


def facto(n):
    if n > 2:
        return n * facto(n - 1)
    else:
        return 2


############################

def isprime(N):
    n=int(N**0.5)            # Permet de gagner en complexité
    for i in range(2,n+1):
        if N%i == 0:
            return 0         # Stop dès que le chiffre est divisible par uun autre
    return 1

def crible(N):
    L=[]
    for k in range(2, N+1):
        if isprime(k) == 1:
            L.append(k)
    print("Quantité de nombre premiers jusqu'à " + str(N) + " : " + str(len(L)))
    return L


Res = crible(1000000)
Res
