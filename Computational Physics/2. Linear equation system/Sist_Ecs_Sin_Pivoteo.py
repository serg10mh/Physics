# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:16:35 2020

@author: sergi
"""
from numpy import *

print('Dada la matriz de coeficientes del sistema, A, y el vector de términos independientes:')
A=array([[2,-1,1],[-1,1,2],[1,2,-1]],'float') 
b=array([[3],[7],[2]],'float')  
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
