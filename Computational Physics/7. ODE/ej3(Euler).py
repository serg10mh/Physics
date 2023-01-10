# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:56:41 2020

@author: sergi
"""
from numpy import*
from matplotlib.pyplot import*
print('Integración de la ecuación logística.')
print()
print('Método de Euler:')
#definimos el valor inicial de las variables con las que trabajaremos
r=1
k=1
p=10
deltat=0.1
def f(p):
	f=1-p/k
	return f
for i in range(100):
	tnew=t+deltat
	pnew=p+deltat*r*f(p)
	p=pnew
	t=tnew
	plot(t,p,'*r')
	xlabel('Tiempo')
	ylabel('Población')
