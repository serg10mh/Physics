# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:26:14 2020

@author: sergi
"""
from numpy import*
#Regla del trapecio
#definimos la función y los puntos inicial y final
a=0
b=1.35
n=1
tolerancia=1e-5
#Regla compuesta del trapecio
def trapecio(a,b,n):
	def f(x):
		y=(x**3)-(3*x**2)-x+3
		return y
	fa=f(a)
	fb=f(b)
	h=(b-a)/n
	x=linspace(a,b,n)
	suma=0
	for i in range(1,n,1):
		aux=f(x[i])
		suma=suma+aux
	I=(h/2)*(fa+fb)+h*(suma)
	return I
error=abs(trapecio(a,b,n+1)-trapecio(a,b,n))
while error>tolerancia:
	n=n+1
	t=trapecio(a,b,n+1)
	error=abs(trapecio(a,b,n+1)-trapecio(a,b,n))
print ('Valor de la integral entre a y b: %.6f' %t)
print('Número de subintervalos:', n)
