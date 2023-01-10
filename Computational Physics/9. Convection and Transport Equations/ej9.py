# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de transporte.')
#método implícito

#valores de los parámetros 
N=20 
dimt=1000
deltat=0.01
deltax=0.3
u=1
C=u*deltat/deltax
s=alfa*deltat/(deltax*deltax)

T=np.zeros(N+1) 
Tnew=np.zeros(N+1)
T=np.vstack(T) #esta vez los defino como columnas para hacer el producto matricial
Tnew=np.vstack(Tnew)

#matriz A
A=np.zeros((N+1,N+1))

T[5:10]=50 #condición inicial
T[15:17]=20
#condiciones de frontera: flujo nulo
T[0]=T[1]
T[N]=T[N-1]

plt.close('all')
plt.figure(1)
plt.plot(T) 
plt.pause(0.1)

#redefinimos A y la invertimos
for i in range(N):
	A[i,i]=1+2*s
	A[i+1,i]=-(1/2)*C-s
	A[i,i+1]=(1/2)*C-s
A[0,0]=1 #redefinimos los términos que no cumplen el bucle
A[N,N]=1
A[0,1]=0
A[N,N-1]=0

Ainv=np.linalg.inv(A)

#realizamos el producto y ploteamos
for i in range(dimt):
	Tnew=np.dot(Ainv,T)
	for k in range(N+1): #bucle de redefinición de variables
		T[k]=Tnew[k]
	#condiciones de frontera: flujo nulo
	T[0]=T[1]
	T[N]=T[N-1]
	if i%10==0:
		plt.figure(1)
		plt.plot(T)
		plt.pause(0.01)
		plt.show

plt.xlabel('Espacio')
plt.ylabel('Temperatura')

