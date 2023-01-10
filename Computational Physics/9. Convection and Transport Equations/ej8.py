# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de transporte.')
#Esquema Dufort-Frankel

#valores de los parámetros 
N=20 
dimt=1000
deltat=0.01
deltax=0.5
u=1
C=u*deltat/deltax

T=np.zeros(N+1)
Tnew=np.zeros(N+1)
Told=np.zeros(N+1)

T[5:10]=10 #condición inicial
Tnew[0]=T[1] #condiciones de frontera: flujo nulo
Tnew[N]=T[N-1]

plt.close('all')
plt.figure(1)
plt.plot(T) 
plt.pause(0.1)

for j in range(dimt): #bucle temporal
	Tnew[0]=T[1] #condiciones de frontera: flujo nulo
	Tnew[N]=T[N-1]
	for i in range(1,N): #bucle espacial
		Tnew[i]=2*s/(1+2*s)*(T[i-1]-Told[i]+T[i+1])-C/(1+2*s)*(T[i+1]-T[i-1])+Told[i]/(1+2*s)
	for k in range(N+1): #bucle de redefinición de variables
		Told[k]=T[k] 
		T[k]=Tnew[k]

	if j%10==0:
		plt.figure(1)
		plt.plot(T)
		plt.pause(0.01)
		plt.show

plt.xlabel('Espacio')
plt.ylabel('Temperatura')

