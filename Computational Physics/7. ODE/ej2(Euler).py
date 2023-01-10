# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:34:39 2020

@author: sergi
"""
print('Integración de la ecuación diferencial del oscilador armónico amortiguado y forzado.')
print()
print('Método de Euler:')
#condiciones iniciales
x=1
y=1
t=0
#parámetros
deltat=0.1
w0=1
b=0.1
F=1
w=1
def f(t,x,y):
	f=y
	return f
def g(t,x,y):
	g=-w0**2*x-b*y+F*cos(w*t)
	return g
clf()
for i in range(250):
	tnew=t+deltat
	xnew=x+deltat*f(t,x,y)
	ynew=y+deltat*g(t,x,y)
	x=xnew 
	y=ynew
	t=tnew
	plot(x,y,'*r')
	xlabel('x')
	ylabel('y')
	title('Euler')
