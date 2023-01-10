# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:39:36 2020

@author: sergi
"""

#SESIÓN 1 COMPUTACIONAL

from numpy import*
from matplotlib.pyplot import*

x=linspace(-2,4,21) #generar una lista de 11 elementos igualmente espaciados entre 0 y 100
def funcion(x):
    y=x*x-3*x+exp(x)-2
    return y
y=funcion(x)

lista=[]
for i in range(len(x)):
	if sign(funcion(x[i-1])) != sign(funcion(x[i])):
		print ('Hay una raíz entre %.4f y %.4f' % (x[i-1],x[i]) )
		cmin=x[i-1]
		cmax=x[i]
		lista.append(cmin)
		lista.append(cmax)
	
plot(x,y, color='red')
axhline(0)
grid(False)
xlabel('x'); ylabel('y');title('y=x^2-3x+e^x-2')





















