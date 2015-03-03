a = [0,0]
b = [4,30]
c = [10,40]
d = [11,10]
e = [17,20]
f = [17,50]

def bonjour(L):
	L[1] += 10
	if L[1] == 60:
		L[0] += 1
		L[1] = 0									
		if L[0] >= 24:
			L[0] = 0
	return(L)

p = 6*24
for g in range(p-1):
	print(bonjour(a)),
	print(bonjour(b)),
	print(bonjour(c)),
	print(bonjour(d)),
	print(bonjour(e)),
	print(bonjour(f))
	
