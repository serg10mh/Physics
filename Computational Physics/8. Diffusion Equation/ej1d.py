# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de difusión del calor en 1 dimensión.')

#valores de los parámetros 
N=20 
dimt=1000
deltat=0.1
deltax=0.5
alfa=1 

T=np.zeros(N+1) 
Tnew=np.zeros(N+1)

T[3:9]=10 #condiciones inciales
T[12:15]=5
Tnew[0]=T[1] #condiciones de frontera: flujo nulo
Tnew[N]=T[N-1]

#ploteo de la condición inicial
plt.close('all')
plt.figure(1)
plt.plot(T,'-r') 
plt.pause(0.1)

for j in range(dimt): 
	for i in range(1,N): 
		Tnew[i]=T[i]+(alfa*deltat)/(deltax*deltax)*(T[i-1]-2*T[i]+T[i+1])
	#condiciones de frontera de flujo nulo
	Tnew[0]=T[1]
	Tnew[N]=T[N-1]
	for i in range(0,N+1): 
		T[i]=Tnew[i]

	if j%10==0:
		plt.figure(1)
		plt.plot(T)
		plt.pause(0.01)
		plt.show

plt.xlabel('Espacio')
plt.ylabel('Tiempo')


