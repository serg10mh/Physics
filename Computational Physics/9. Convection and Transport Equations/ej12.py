# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de transporte en 2D.')
#Esquema FCTS

#valores de los parámetros 
N=10
dimt=1000
deltat=0.01
deltax=0.6
deltay=0.4
alfax=1.5
alfay=2.5
#valores en la frontera
phi=np.random.rand()*2*np.pi
a=np.sin(phi)
b=5*np.sin(phi)
c=5*np.cos(phi)
d=np.cos(phi)

T=np.zeros((N+1,N+1))
Tnew=np.zeros((N+1,N+1))

T[9:11,5:17]=50 #condición incial
Tnew[0,:]=a #condiciones de contorno
Tnew[N,:]=b
Tnew[:,0]=c
Tnew[:,N]=d

#ploteo de la condición inicial y las condiciones de frontera
plt.close('all')
plt.figure(1)
plt.imshow(T, cmap='hot') 
plt.pause(0.1)

for j in range(dimt):
	for i in range(1,N):
		for k in range(1,N):
			Tnew[i,k]=T[i,k]+(alfax*deltat/(deltax*deltax))*(T[i-1,k]-2*T[i,k]+T[i+1,k])+(alfay*deltat/(deltay*deltay))*(T[i,k-1]-2*T[i,k]+T[i,k+1])
	Tnew[0,:]=a #condiciones de contorno
	Tnew[N,:]=b
	Tnew[:,0]=c
	Tnew[:,N]=d
	for i in range(0,N+1):
		for k in range(0,N+1):
			T[i,k]=Tnew[i,k]
	if j%10==0:
		plt.figure(1)
		plt.imshow(T, cmap='hot')
		plt.pause(0.01)
		plt.show

