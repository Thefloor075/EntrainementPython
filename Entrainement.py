from math import *

def hms(N):
	L = [0,0,0]
	while N!=0:
		if N > 3600:
			N -= 3600
			L[0] += 1
		elif N > 60
			N -=60
			L[1] += 1
		elif N > 0
			N -= 1
			L[2] += 1
	return L

def mult(a):

#comprend pas

#T.D.2.

def ordre(x,y,z):
	if z%x == 0:	return True
	else:	return False

def max2(x,y):
	if x > y:
		return x
	else:	return y

def max3(x,y,z):
	return max2(max2(x,y),z)

def racine(a,b,c):
	delta = b**2 - 4*a*c
	if delta == 0:
		return(-b/2*a)
	elif delta > 0:
		return [(-b + sqrt(delta)/(2*a)),(-b - sqrt(delta)/(2*a))]
	else:
		print("Pas de racine réel")


def bissextile(annee):
#FLEMME ..
def function():
	pass
#Flemme Aussi .. 

def date(jour,moi,annee):
	L = [x for x in range(1,13)]
	if moi in not L:
		print("Cette composition de chiffre ne correspond a rien")


def somme(liste):
	s = 0
	for i in range(len(liste)):
		s += somme[i]
	return s

def moyemme(liste):
	return somme(liste)/len(liste)

def carre(liste):
	for i in range(len(n)):
		liste[i] *= liste[i]
	return liste

def pair(liste):
	s = []
	for i in range(len(liste)):
		if liste[i]%2 == 0:
			s.append(s[i])
	return s

def max1(L):
	max1 = L[0]:
	for i in range(len(L)):
		if L[i] > max1:
			max1 = L[i]
	return max1

def min1(L):
	min1 = L[0]
	for i in range(len(L)):
		if L[i] < min1:
			min1 = L[i]
	return min1

def en_commun(L1,L2):
	L = []
	for i in range(len(L2)):
		if L2[i] in L1:
			L.append(L2[i])
	return L

#Exercice 6 pages 24

def suite_ab(n):
	a0 = 3
	b0 = 2
		while n!= 0:
			an = a0 + 2*b0
			bn = a0 + b0
			an,bn = a0,b0
			n -= 1
			un = an/bn
	return un

def seuil_som_car(M):
	n,s = 0,0
	while s <= M:
		s += n**2
		n += 1
	return n

def fact(n):
	u = 1
	while n!=0:
		u *= n
		n -= 1
	return u 

def est_fact(n):
	u = 1
	k = 1
	while n!= 1:
		if n%k == 0:
		    print(n,k,u)
		    n /= k
		    k += 1
		else:
			return False
	return k-1 
			
def inverse(mct):
	return mct[::-1]

def palindrome(mot):
	for i in range(len(mot)):
		if inverse(mot)[i]!=mot[i]:
			return False
	return True

def palindrome_rapide(mot):
	for i in range(len(mot)//2):
		if inverse(mot)[i]!=mot[i]:
			return False
	return True

def zero_liste(L):
	for i in range(len(L)-1):
		L.insert(2*i + 1,0)
	return L

def syr2(u0):
	n = 0
	while u0!=1:
		if u0%2 == 0:
			u0 /= 2
			n+= 1
		else:
			u0 = 3*u0 + 1
			n += 1
	return n 

def fibo_rec(n):
	if n == 0:
		return 1
	else:
		return n*fibo_rec(n-1)

def palindrome_rec(mot):





def puissance_rapide(a,n):
	if n == 0:
		return 1
	elif n%2 == 0:
		return puissance_rapide(a,n/2)**2
	else:
		return a*puissance_rapide(a,(n-1)/2)**2

def modulo(a,b):
	while a > b:
		a -= b
	return a 

def pgcd(a,b):
	if a%b == 0:
		return b
	else:
		return pgcd(b,a%b)

def pgcd_liste(L):




""""""""""""""""""""""""""""""""""""""""""""""""
def premiers(N):
	n = 1
	L = []
	while len(L)! = N:
		if premier1(n) == True:
			L.append(n)
			n += 1
		else:
			n += 1
	return L


def premier1(N):
	racine = int(sqrt(N))
	for i in range(racine + 1):
		if N%i == 0:
			return False
	return True 
""""""""""""""""""""""""""""""""""""""""""""""""

def decomp_premiers(N):
	L = []
	n = 2 
	while N!=1:
		if N%n == 0:
			L.append(n)
			N /= n
			n = 2
		else:
			n += 1
	return L #A Verifier

""""""""""""""""""""""""""""""""""""""""""""""""

def nombre_parfait(n):
	if diviseurs(n)/2 == n:
		return True
	return False


def diviseurs(n):
	s = 0 
	racine = int(sqrt(n))
	for i in range(racine + 1)
		if n%i == 0:
			s += n/i + n/(n/i)
	return s #A Verifier

def tous_les_parfaits(N):
	L = []
	n = 1
	while n!=N:
		if nombre_parfait(n) == True:
			L.append(n)
			n+=1
		else:
			n+=1
	return L 

""""""""""""""""""""""""""""""""""""""""""""""""

#(Longueur d'un nombre) ecrire une fonction long(n)
#qui étant donnée l'écriture decimale de l'netier 
#naturel n = ap ..... ao retourne l'entier p

def long(p):


""""""""""""""""""""""""""""""""""""""""""""""""

def binaire(n):
	L = []
	while n!=0
		if n%2 == 0:
			L.append(0)
			n /= 2
		else:
			L.append(1)
			n //= 2
	return L


#T.D.8

def fahrenheit(celsius):
	return (9/5)*celsius + 32

def ameliorer_fahrenheit(celsius):
	return ((90/50)*celsius + 320)/10 #Partie entier a utiliser

def inverse_fahrenheit(fahrenheit):
	return  (fahrenheit - 32)*(5/9)

def somme(n):
	s = 0
	for i in range(n+1):
		s += i 
	return s

def som_car(n):
	s = 0
	for i in range(n+1):
		s += i**2
	return s

def valid_som_car(n):
	if som_car(n) == (1/6)*n*(n+1)*(2*n + 1)
		return True
	else:
		return False

def N2(n,m):
	for i in range(n+1):
		for j in range(m+1):
			print([i,j])

