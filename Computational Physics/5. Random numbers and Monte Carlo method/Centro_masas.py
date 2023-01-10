# -*- coding: utf-8 -*-

from numpy import *
import random as rnd

#definimos la función densidad de masa superficial
def rho(x,y):
	if (x-6)**2+y**2 < 4:
		r=0
		return r
	else:
		r=1
		return r
def fx(x,y):
	fx=x*rho(x,y)
	return fx
def fy(x,y):
	fy=y*rho(x,y)
	return fy
N=100000
R=2
V=48
sf=0
sf2=0
sfx=0
sf2x=0
sfy=0
sf2y=0
rnd.seed(1)
for i in range(N):
    x=rd.uniform(0,8)
    y=rd.uniform(0,6)
    aux1=densidad(x,y)
    sf=sf+aux1
    sf2=sf2+aux1**2
    aux2=fx(x,y)
    sfx=sfx+aux2
    sf2x=sf2x+aux2**2
    aux3=fy(x,y)
    sfy=sfy+aux3
    sf2y=sf2y+aux3**2
fm=sf/N
fm2=sf2/N
I= (V/N)*sf
E=V*((fm2-fm**2)/N)**(1/2)
fmx=sfx/N
fm2x=sf2x/N
Ix= (V/N)*sfx
Ex=V*((fm2x-fmx**2)/N)**(1/2)
fmy=sfy/N
fm2y=sf2y/N
Iy= (V/N)*sfy
Ey=V*((fm2y-fmy**2)/N)**(1/2)
sxG=((Ex**2/I**2)+((Ix**2*E**2)/I**4))**(1/2)
syG=((Ey**2/I**2)+((Iy**2*E**2)/I**4))**(1/2)
print ('Las coordenadas del centro de masas serán: (%.5f,%.5f)' %(Ix/I , Iy/I))
print('Con una incertidumbre de (%.5f,%.5f)' %(sxG, syG))


