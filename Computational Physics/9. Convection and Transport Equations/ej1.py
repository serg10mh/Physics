# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de convección.')
#Esquema FCTS

#valores de los parámetros 
N=20 
dimt=1000
deltat=0.01
deltax=0.5
u=0.5
C=u*deltat/deltax

T=np.zeros(N+1)
Tnew=np.zeros(N+1)

T[9:11]=10 #condición incial

Tnew[0]=T[1] #condiciones de frontera: flujo nulo
Tnew[N]=T[N-1]

plt.close('all')
plt.figure(1)
plt.plot(T) 
plt.pause(0.1)

for j in range(dimt):
	for i in range(1,N):
		Tnew[i]=T[i]-(1/2)*C*(T[i+1]-T[i-1])
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

