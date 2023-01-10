# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:01:32 2020

@author: sergi
"""

x=linspace(-2,4,21) #generar una lista de 11 elementos igualmente espaciados entre 0 y 100
def funcion(x):
    y=x*x-3*x+exp(x)-2
    return y
y=funcion(x)
#def recta(x):
#	f=funcion(min(x))+((funcion(max(x))-funcion(min(x))/(max(x)-min(x))*(x-min(x)))
#	return f
lista=[]
for i in range(len(x)):
	if sign(funcion(x[i-1])) != sign(funcion(x[i])):
		print ('Hay una raíz entre %.6f y %.6f'% (x[i-1],x[i]) )
		cmin=x[i-1]
		cmax=x[i]
		lista.append(cmin)
		lista.append(cmax)

error=0.000001
xaux1=[lista[0]]
xaux2=[lista[2]]

