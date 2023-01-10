# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 23:57:12 2020

@author: sergi
"""
from numpy import *
#pivoteo parcial
print('Dada la matriz de coeficientes del sistema, A, y el vector de términos independientes:')
A=array([[1,2,-1],[2,4,5],[3,-1,-2]],'float') 
b=array([[2],[25],[-5]],'float')
print('')
print('Construyo la matriz ampliada, Ab:')
Ab=hstack((A,b))
print('')
nf,nc=Ab.shape
#Para n ecuaciones:
for j in range(nf):
		for i in range(j+1,nf):
			Ab[i,:]=Ab[i,:]-((Ab[j,:])*(Ab[i,j]/Ab[j,j]))
for i in range(nf-1):
	max=argmax(abs(Ab[:,i]))
	