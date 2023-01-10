# -*- coding: utf-8 -*-

from numpy import*

print('Método de Jacobi')
print()
n=3 #orden matriz
#Definimos la matriz A y la identidad
A=array([[3,-1,0],[-1,2,-1],[0,-1,3]])
I=zeros([n,n])
for i in range(n):
	for j in range(n):
		if i == j:
			I[i,j]=1
		else:
			I[i,j]=0
#Definimos ahora la precisión
E=1e-7
dc=copy(I)
vc=copy(I)
#Definimos las matrices D y V
D0=copy(A)
V0=copy(I)
F=False
while F==False:
    F=all(dc<E) and all(vc<E)
    z=0
    for i in range(n):
        for j in range(n):
            if i != j:
				if abs(D0[i,j]) > abs(z):
					z=D0[i,j]
					p=i
					q=j
	#Definimos los parámetros del método de Jacobi
	theta=(D0[q,q]-D0[p,p])/(2*D0[p,q])
	signo=0
	if theta >= 0:
		signo=1
	else:
		signo=-1
	t=signo/(abs(theta)+(theta**2+1)**(1/2))
	c=1/(t**2+1)**(1/2)
	s=c*t
	#Definimos R, R traspuesta y redefinimos D y V
	R=copy(I)
	R[p,p]=c
	R[p,q]=s
	R[q,p]=-s
	R[q,q]=c
	Rt=zeros([n,n])
	for i in range(n):
		for j in range(n):
			if i != j:
				Rt[i,j]=R[j,i]
			if i == j:
				Rt[i,j]=R[i,j]
	Daux=dot(Rt,D0)
	D=dot(Daux,R)
	V=dot(V0,R)
	dc=abs(D-D0)
	vc=abs(V-V0)
	#Redefinimos los valores iniciales de D y V
	D0=copy(D)
	V0=copy(V)
a=[]
for k in range(n):
    a.append(D[k,k])  
print('Autovalores:') 
for l in range(n):
	print('%.8f' %a[l])
print('Autovectores, por columnas:')
print(V)






			

