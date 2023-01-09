# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:30:03 2020

@author: sergi
"""
from numpy import*
from matplotlib.pyplot import*

x=linspace(-2,4,21) #generar una lista de 11 elementos igualmente espaciados entre 0 y 100
def funcion(x):
    y=x*x-3*x+exp(x)-2
    return y
y=funcion(x)
def derivada(x):
	y=2*x-3+exp(x)
	return y

print ('Buscamos los intervalos en los que puede haber una raíz')

lista=[]
for i in range(len(x)):
	if sign(funcion(x[i-1])) != sign(funcion(x[i])):
		print ('Hay una raíz entre %.6f y %.6f'% (x[i-1],x[i]) )
		cmin=x[i-1]
		cmax=x[i]
		lista.append(cmin)
		lista.append(cmax)

print('Determinamos las raíces por el método de Newton')

error=0.000001
k=0
l=0
xaux1=[lista[0]]
xaux2=[lista[2]]
while abs(funcion(xaux1[k])) > error:
	xaux1.append(xaux1[k]-(funcion(xaux1[k])/derivada(xaux1[k])))
	k=k+1
while abs(funcion(xaux2[l])) > error:
	xaux2.append(xaux2[l]-(funcion(xaux2[l])/derivada(xaux2[l])))
	l=l+1
print ('Raíz en %.6f' % (xaux1[k]))
print ('Raíz en %.6f' % (xaux2[l]))

plot(x,y, color='red')
axhline(0)
grid(False)
xlabel('x'); ylabel('y');title('y=x^2-3x+e^x-2')









