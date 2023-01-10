# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:39:42 2020

@author: sergi
"""
from numpy import*
from matplotlib.pyplot import*
print('Integración de la ecuación logística.')
print()
print('Método de Runge-Kutta (4º orden):')
r=1
k=1
p=10
deltat=0.1
def f(p):
	f=1-p/k
	return f
for i in range(100):
	tnew=t+deltat
	k1=deltat*r*f(p)
	k2=deltat*r*f(p+k1/2)
	k3=deltat*r*f(p+k2/2)
	k4=deltat*r*f(p+k3)
	pnew=p+k1/6+k2/3+k3/3+k4/6
	p=pnew
	t=tnew
	plot(t,p,'*r')
	xlabel('Tiempo')
	ylabel('Población')
