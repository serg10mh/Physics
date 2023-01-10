# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:31:26 2020

@author: sergi
"""

import numpy as np

x=linspace(-2,4,100)
def funcion(x):
	f=x*x-3*x+exp(x)-2
	return f
a=-2
b=4
error=0.000001
v=[]
intervalo=b-a
fa= funcion(a)
fb= funcion(b)
i=1
while intervalo > error:
	c= (a+b)/2
	fc= funcion(c)
	v.append([i,a,c,b,fa,fb,intervalo])
	i=i+1

	signo=np.sign(fa)*np.sign(fc)
	if signo<0:
		b=cfb=fc
	else:
		a=cfa=fc
	intervalo = b-a
c=(a+b)/2
fc=funcion(c)
v.append([i,a,c,b,fa,fc,fb,intervalo])
v=np.array(v)

raiz=c

print ('Raiz, c= ', raiz)
y=funcion(x)
plot(x,y)
grid(False)
xlabel('x');ylabel('f(x)')
















