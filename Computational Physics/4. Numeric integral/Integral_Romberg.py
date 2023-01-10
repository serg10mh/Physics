# -*- coding: utf-8 -*-

from numpy import*
from math import* 

#trapecio recursivo
a=0
b=(pi/2)
E=1e-8 #precision
def f(x):
	y=(x**2+x+1)*(cos(x))
	return y
S=((b-a)/2)*(f(a)+f(b)) #valor inicial
T1=[]
T1.append([A])
E1=1
E2=2
j=1 #punto de partida
while abs(E2-E1)>E:
    j=j+1
    n=int(2**(j-2))
    T=(S/2)
    h=(b-a)/(2**(j-1))
    for k in range(1,n+1):
        x=a+(2*k-1)*h
        T=T+h*f(x)
    S=T
    T1.append(T)
    T0=zeros((j,1))
    #Transponemos T1
    for i in range(j):
        T0[i]=T1[i]
    #Regla de Romberg
    R=zeros((j,j))
    for i in range(j):
    	R[i,0]=T0[i]
    for k in range(1,j):
        for i in range(k,j):
            R[i,k]=(4**(k)*R[i,k-1]-R[i-1,k-1])/(4**(k)-1)
    E1=R[j-2,j-2]
    E2=R[j-1,j-1]
print('Matriz de Romberg:')
print(R)
print('La integral entre %f y %f es : %.10f' %(a,b,E2))