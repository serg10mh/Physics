# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:08:42 2020

@author: sergi
"""
from numpy import*
from matplotlib.pyplot import*

print('Integración de la ecuación diferencial del oscilador armónico.')
print()
print('Método de Runge-Kutta(2º orden):')
x=1
y=1
t=0
deltat=0.1
w0=1
def f(t,x,y):
	f=y
	return f
def g(t,x,y):
	g=-w0**2*x
	return g
for i in range(100):
	tnew=t+deltat
	k1x=deltat*f(t,x,y)
	k1y=deltat*g(t,x,y)
	k2x=deltat*f(t+deltat/2,x+k1x/2,y+k1y/2)
	k2y=deltat*g(t+deltat/2,x+k1x/2,y+k1y/2)
	xnew=x+k2x
	ynew=y+k2y
	x=xnew
	y=ynew
	t=tnew
	plot(x,y,'r*')
	xlabel('x')
	ylabel('y')
	title('RK2')

