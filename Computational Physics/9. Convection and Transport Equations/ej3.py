# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de convección.')
#Esquema Dufort-Frankel

#valores de los parámetros 
N=20 
dimt=1000
deltat=0.01
deltax=0.7
u=1
C=u*deltat/deltax

T=np.zeros(N+1)
Tnew=np.zeros(N+1)
Told=np.zeros(N+1)

T[5:10]=10 #condiciones iniciales
T[12:18]=45
Tnew[0]=5 #condiciones de frontera
Tnew[N]=15

plt.close('all')
plt.figure(1)
plt.plot(T)
plt.pause(0.1)

for j in range(dimt): #bucle temporal
	for i in range(1,N): #bucle espacial
		Tnew[i]=Told[i]-C*(T[i+1]-T[i-1])
	Tnew[0]=5 #condiciones de frontera
	Tnew[N]=15
	for k in range(N+1): #bucle de redefinición de variables
		Told[k]=T[k]
		T[k]=0.5*(T[k]+Tnew[k])

	if j%10==0:
		plt.figure(1)
		plt.plot(T)
		plt.pause(0.01)
		plt.show

plt.xlabel('Espacio')
plt.ylabel('Temperatura')

