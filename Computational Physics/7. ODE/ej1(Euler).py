# -*- coding: utf-8 -*-
from numpy import*
from matplotlib.pyplot import*

print('Integración de la la ecuación diferencial del oscilador armónico.')
print()
print('Método de Euler:')
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
	xnew=x+deltat*f(t,x,y)
	ynew=y+deltat*g(t,x,y)
	x=xnew 
	y=ynew
	t=tnew
	plot(x,y,'*r')
	xlabel('x')
	ylabel('y')
	title('Euler')

