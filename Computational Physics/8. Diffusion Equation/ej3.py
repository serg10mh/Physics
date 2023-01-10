# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

print('Ecuación de difusión del calor en 1 dimensión.')
#Esquema a dos niveles temporales y centrado en el espacio

#valores de los parámetros 
N=20 
dimt=1000
deltat=0.01
deltax=0.7
alfa=1 

T=np.zeros(N+2)
Tnew=np.zeros(N+2)

T[9:11]=10 #condición inicial

T[0]=5 #condiciones de frontera
T[N]=3
T[N+1]=3
#ploteo de la condición inicial y las condiciones de frontera
plt.close('all')
plt.figure(1)
plt.plot(T,'-r') 
plt.pause(0.1)

for i in range(dimt): #bucle temporal
	#condiciones de frontera
	Tnew[0]=5
	Tnew[N]=3
	Tnew[N+1]=3 	
	for j in range(1,N): #bucle espacial
		Tnew[j]=T[j]+(deltat*alfa/(deltax*deltax))*(-(1/12)*T[j-2]+(4/3)*T[j-1]-(5/2)*T[j]+(4/3)*T[j+1]-(1/12)*T[j+2])   
	for k in range(N+1): #bucle de redefinición de variables
		T[k]=Tnew[k]
	if i%10==0:
		plt.figure(1)
		plt.plot(T)
		plt.pause(0.01)
		plt.show

plt.xlabel('Espacio')
plt.ylabel('Temperatura')

