# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de difusión del calor en 1 dimensión.')
#Esquema Dufort-Frankel

#valores de los parámetros 
N=20 
dimt=1000
deltat=0.01
deltax=0.7
alfa=1 
s=alfa*deltat/(deltax*deltax)

T=np.zeros(N+1)
Tnew=np.zeros(N+1)
Told=np.zeros(N+1)

T[9:11]=10 #condición inicial
Tnew[0]=5 #condiciones de frontera
Tnew[N]=3

#ploteo de la condición inicial y las condiciones de frontera
plt.close('all')
plt.figure(1)
plt.plot(T,'-r') 
plt.pause(0.1)

for j in range(dimt): #bucle temporal
	#condiciones de frontera
	Tnew[0]=5
	Tnew[N]=3
	for i in range(1,N): #bucle espacial
		Tnew[i]=(2*s/(1+2*s))*(T[i-1]+T[i+1])+((1-2*s)/(1+2*s))*Told[i]
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