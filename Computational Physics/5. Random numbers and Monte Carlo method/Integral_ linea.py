# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:20:47 2020

@author: sergi
"""
from numpy import*
import  random as rnd
from time import time

t1=time()
N=100000 #número de puntos
a=0
b=1
V=b-a
def f(x):
	y=(1-x**2)**(3/2)
	return y
suma1=0
suma2=0
for i in range(N):
	x=rnd.uniform(a,b)
	aux=f(x)
	suma1=suma1+aux
	suma2=suma2+(aux**2)
prom1=suma1/N
prom2=suma2/N
I=V*prom1
E=V*((prom2-prom1**2)/N)**(1/2)
t2=time()
tiempo=t2-t1
print ('El valor de la integral es %.5f con un error de %.5f' %(I,E))
print ('El tiempo de ejecución para %.f ha sido %.2e segundos' %(N,tiempo))
