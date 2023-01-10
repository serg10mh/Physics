# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de transporte.')
#Esquema upstream

#valores de los parámetros 
N=20 
dimt=1000
deltat=0.01
deltax=0.5
u=1
C=u*deltat/deltax
alfa=1
s=alfa*deltat/(deltax*deltax)

T=np.zeros(N+1)
Tnew=np.zeros(N+1)

T[5:10]=10 #condiciones iniciales
T[12:15]=15

plt.close('all')
plt.figure(1)
plt.plot(T) 
plt.pause(0.1)

for j in range(dimt):
	for i in range(1,N):
		Tnew[i]=(1-C)*T[i]+C*T[i-1]+(alfa*(T[i-1]-2*T[i]+T[i+1])/(deltax*deltax))*deltat
	Tnew[0]=5 #condiciones de frontera
	Tnew[N]=0
	for i in range(0,N+1):
		T[i]=Tnew[i]

	if j%10==0:
		plt.figure(1)
		plt.plot(T)
		plt.pause(0.01)
		plt.show
        
plt.xlabel('Espacio')
plt.ylabel('Temperatura')

