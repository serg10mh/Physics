# -*- coding: utf-8 -*-

from numpy import *

#Resolvemos primero el sistema de ecuaciones (implemento el programa del tema anterior)
print('Dada la matriz de coeficientes del sistema, A, y el vector de términos independientes:')
A=array([[1,1,1],[-1,0,1],[1,0,1]],'float') 
b=array([[0],[1],[0]],'float')   
print ('A= ')
print(A)
print ('b= ')
print(b)
print('')
print('Construyo la matriz ampliada, Ab:')
Ab=hstack((A,b))
print(Ab)
print('')
nf,nc=Ab.shape 
#Para n ecuaciones:
for j in range(nf):
	for i in range(j+1,nf):
		Ab[i,:]=Ab[i,:]-((Ab[j,:])*(Ab[i,j]/Ab[j,j]))
print('Sistema triangular superior:' )
print(Ab)
print('')
#Sustitución regresiva
x=zeros((nf,1), 'float')
for i in range(nf-1,-1,-1):
	suma=dot(Ab[i,0:nf], x)
	x[i]=((Ab[i,nc-1]-suma)/(Ab[i,i]))
print('Soluciones del sistema:')
for i in range(nf):
	print('x(%i)= %.2f' % ((i,x[i])) )
#calculamos la derivada

#calculamos la derivada
def f(x):
	y=8*x**4-3*x**2+2*x+5
	return y
h=0.001
x0=2.0
#k=1 orden de la derivada
#ecuación 10
aux1=f(x0+h)-f(x0-h)
f1=aux1/(2*h)
print('')
print('Derivada primera en %.4f= %.4f' %(x0,f1))

