# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de convección.')
#método implícito

#valores de los parámetros 
N=5
dimt=1000
deltat=0.01
deltax=0.5
u=1
C=u*deltat/deltax

T=np.zeros(N+1) 
Tnew=np.zeros(N+1)
T=np.vstack(T) #esta vez los defino como columnas para hacer el producto matricial
Tnew=np.vstack(Tnew)

#matriz A
A=np.zeros((N+1,N+1))

T[5:10]=10 #condición inicial

plt.close('all')
plt.figure(1)
plt.plot(T) 
plt.pause(0.1)

#redefinimos A y la invertimos
for i in range(N):
	A[i,i]=1
	A[i+1,i]=-(1/2)*C
	A[i,i+1]=(1/2)*C
A[0,0]=1 #redefinimos los términos que no cumplen el bucle
A[N,N]=1
A[0,1]=0
A[N,N-1]=0

Ainv=np.linalg.inv(A)

for i in range(dimt):
	Tnew=np.dot(Ainv,T)
	for k in range(N+1): #bucle de redefinición de variables
		T[k]=Tnew[k]
	#condiciones de frontera
	T[0]=5
	T[N]=15
	if i%10==0:
		plt.figure(1)
		plt.plot(T)
		plt.pause(0.01)
		plt.show

plt.xlabel('Espacio')
plt.ylabel('Temperatura')

