"""
Intersection example
"""
#Examen de evaluación 3D, Andrei Enrique Carvajal Brito, 27/01/2021
#No. control: 1839022
#importa libreria
import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import tools3D as tools3d

#______Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=80
yc=40
zc=40

#Plano y linea de sistema
x=[-40,-40,40,40,-40,-20]
y=[0,0,0,0,-20,-10]
z=[-10,10,10,-10,15,0]

for i in range(len(x)):
    xg.append(x[i]+xc)
    yg.append(y[i]+yc)
    zg.append(z[i]+zc)

#____Plotear el sistema 
#def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
    plt.axis([0,150,100,0])
    plt.axis('on')
    plt.grid(True)
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')#plano
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='k')
    #plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='k')
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='k')
    plt.plot([xg[4],xg[5]],[yg[4],yg[5]],color='b')#Line

    if hitcolor=='g':# Do not touch hit point
        plt.scatter(xg[5],yg[5],s=20,color=hitcolor)
    else:
        plt.scatter(xhg,yhg,s=20,color=hitcolor)

    plt.show()

def hitpoint(x,y,z):
    #_____distance point 4 to 5
    a=x[5]-x[4]
    b=y[5]-y[4]
    c=z[5]-z[4]
    Q45=sqrt(a*a+b*b+c*c) 
    # unit vector components point 4 to 5
    lx=a/Q45 
    ly=b/Q45
    lz=c/Q45
    #_____distance point 0 to 3
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    Q03=sqrt(a*a+b*b+c*c) 
    # unit vector components point 0 to 3
    ux=a/Q03 #———unit vector 0 to 3
    uy=b/Q03
    uz=c/Q03
    #_____distance point 0 to 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=sqrt(a*a+b*b+c*c)
    # unit vector components point 0 to 1
    vx=a/Q01 #———unit vector 0 to 1
    vy=b/Q01
    vz=c/Q01
    #_____normal vector unit
    nx=uy*vz-uz*vy 
    ny=uz*vx-ux*vz
    nz=ux*vy-uy*vx
    #___________vector components 0 t0 4
    vx1b=x[4]-x[0]
    vy1b=y[4]-y[0]
    vz1b=z[4]-z[0]
    #____perpenticular distance 4 to plane
    Qn=(vx1b*nx+vy1b*ny+vz1b*nz)

    #_____cos of angle p
    cosp=lx*nx+ly*ny+lz*nz

    #___distance 4 to hit point
    Qh=abs(Qn/cosp)

    #____Hit point coordinates
    xh=x[4]+Qh*lx
    yh=y[4]+Qh*ly
    zh=z[4]+Qh*lz

    #_____global hit point coodinates
    xhg=xh+xc
    yhg=yh+yc
    zhg=zh+zc
    #________checar si la linea de 4 A 5 queda fuera de los valores del rectangulo
    #____Component of vector V0h
    a=xh-x[0]
    b=yh-y[0]
    c=zh-z[0]
    #dot products
    up=a*ux+b*uy+c*uz
    vp=a*vx+b*vy+c*vz
    #Si no estamos saliendo del plano del objeto rectangulo 
    hitcolor='r'
    if up<0:
        hitcolor='b'
    if up>Q03:
        hitcolor='b'
    if vp<0:
        hitcolor='b'
    if vp>Q01:
        hitcolor='b'
    
    #_____Si el punto de 4 a 5 no alcanza el hit point
    a=x[5]-x[4]
    b=y[5]-y[4]
    c=z[5]-z[4]
    Q45=sqrt(a*a+b*b+c*c)
    if Q45 < Qh:
        hitcolor='g'
    return xh,yh,xhg,yhg,hitcolor 


def plotPlaneLinex(xc,yc,zc,Rx):
    for i in range(len(y)):
        [xg[i],yg[i],zg[i]]=tools3d.rotRx(xc,yc,zc,x[i],y[i],z[i],Rx)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)

def plotPlaneLiney(xc,yc,zc,Ry):
    for i in range(len(y)):
        [xg[i],yg[i],zg[i]]=tools3d.rotRy(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)

def plotPlaneLinez(xc,yc,zc,Rz):
    for i in range(len(y)):
        [xg[i],yg[i],zg[i]]=tools3d.rotRz(xc,yc,zc,x[i],y[i],z[i],Rz)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)
    

####_____pedir al usaurio que eje desea trabajar y plotear el PlaneLine
while True:
    axis=input("Teclea el eje que deseas visualizar 'x,y,z' o pulsa 18390022 para salir ?:")
    if axis=='x':#plotear el eje X
        Rx=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinex(xc,yc,zc,Rx)#LLamamos a la funcion de ploteo
    if axis=='y':
        Ry=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLiney(xc,yc,zc,Ry)#LLamamos a la funcion de ploteo
    if axis=='z':
        Rz=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinez(xc,yc,zc,Rz)#LLamamos a la funcion de ploteo
    if axis== '18390022':
        break

