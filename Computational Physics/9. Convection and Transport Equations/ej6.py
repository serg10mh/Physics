# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de transporte.')
#Esquema FCTS

#valores de los parámetros 
N=20 
dimt=1000
deltat=0.01
deltax=0.5
u=1
C=u*deltat/deltax
alfa=1

T=np.zeros(N+1)
Tnew=np.zeros(N+1)

T[9:11]=10 #condición inicial

Tnew[0]=T[1] #condiciones de frontera: flujo nulo
Tnew[N]=T[N-1]

plt.close('all')
plt.figure(1)
plt.plot(T) 
plt.pause(0.1)

for j in range(dimt):
	for i in range(1,N):
		Tnew[i]=deltat*alfa*(T[i-1]-2*T[i]+T[i+1])/(deltax**2)-deltat*u*(T[i+1]-T[i-1])/(2*deltax)+T[i]
	Tnew[0]=T[1] #condiciones de frontera: flujo nulo
	Tnew[N]=T[N-1]
	for i in range(0,N+1): 
		T[i]=Tnew[i]

	if j%10==0:
		plt.figure(1)
		plt.plot(T)
		plt.pause(0.01)
		plt.show

plt.xlabel('Espacio')
plt.ylabel('Temperatura')

