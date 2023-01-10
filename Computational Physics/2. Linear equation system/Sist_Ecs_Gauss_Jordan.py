# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:02:54 2020

@author: sergi
"""
from numpy import * 
from numpy.linalg import * 

print('Dada la matriz de coeficientes del sistema, A, y el vector de términos independientes:')
A=array([[1,2,-1],[2,4,5],[3,-1,-2]],'float') 
b=array([[2],[25],[-5]],'float')  
print ('A= ')
print(A)
print ('b= ')
print(b)
print('')
print('Construyo la matriz ampliada, Ab:')
Ab=hstack((A,b))
print(Ab)
nf,nc=Ab.shape 

for i in range(nf-1):
	for j in range()