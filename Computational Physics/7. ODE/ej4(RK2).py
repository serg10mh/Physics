# -*- coding: utf-8 -*-

from numpy import*
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

print('Integración del modelo de Lorentz por el método de Runge-Kutta (2º orden).')
print('')
#parámetros
sigma=3
r=26.5
b=1
deltat=0.0001
#número de iteraciones
n=100000
#vectores para almacenar los puntos espaciales
X=[] ; Y=[] ; Z=[] ; T=[]
#condiciones iniciales
x=0 ; y=1 ; z=0 ; t=0 
#sistema de ecuaciones
def f(t,x,y,z): #dx/dt=f
    f=sigma*(y-x)
    return f
def g(t,x,y,z): #dy/dt=g
    g=r*x-y-x*z
    return g
def h(t,x,y,z): #dz/dt=h
    h=x*y-b*z
    return h
 
X.append(x)
Y.append(y)
Z.append(z)
T.append(t)

for i in range(n):
	tnew=t+deltat
	k1x=deltat*f(t,x,y,z)
	k1y=deltat*g(t,x,y,z)
	k1z=deltat*h(t,x,y,z)
	k2x=deltat*f(t+deltat/2,x+k1x/2,y+k1y/2,z+k1z/2)
	k2y=deltat*g(t+deltat/2,x+k1x/2,y+k1y/2,z+k1z/2)
	k2z=deltat*h(t+deltat/2,x+k1x/2,y+k1y/2,z+k1z/2)
	xnew=x+k2x
	ynew=y+k2y
	znew=z+k2z
	x=xnew
	y=ynew
	z=znew
	t=tnew
	X.append(x)
	Y.append(y)
	Z.append(z)
	T.append(t)

print('Variables espaciales respecto al tiempo:')
print('')

plt.plot(X,T)
plt.xlabel('t')
plt.ylabel('x')
plt.title('Coordenada x')
plt.show()

plt.figure()
p2=plt.plot(Y,T)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Coordenada y')
plt.show()

plt.figure()
p3=plt.plot(Z,T)
plt.xlabel('t')
plt.ylabel('z')
plt.title('Coordenada z')
plt.show()

print('')
print('Gráfico tridimensional: Espacio vs tiempo')
print('')

X=array([X])
Y=array([Y])
Z=array([Z])
T=array([T])
plt.close('all')
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_wireframe(X, Y, Z, color='firebrick')
ax.set_title('RK2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()