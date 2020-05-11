from graphics import *
from primitives import *
from fill import *
from math import sqrt
import numpy as np
colors=["red","red","red","red","red","red"]

def perspective(cube,cop,x,n):
    x0,y0,z0= x[0],x[1],x[2]
    a,b,c = cop[0],cop[1],cop[2]
    n1,n2,n3 = n[0],n[1],n[2]
    d0 = x0*n1 + y0*n2 + z0*n3
    d1 = a*n1 + b*n2 + c*n3
    d = d0-d1
    T=np.zeros((4,4))
    T[0][0],T[0][1],T[0][2],T[0][3] = n1*a + d , b*n1 , c*n1 , n1
    T[1][0],T[1][1],T[1][2],T[1][3] = a*n2 , b*n2 + d , c*n2 , n2
    T[2][0],T[2][1],T[2][2],T[2][3] = a*n3 , b*n3 , c*n3 + d , n3
    T[3][0],T[3][1],T[3][2],T[3][3] = -a*d0 , -b*d0 , -c*d0 , -d1
    prj=[]
    for i in range(0,6):
        p=np.array(cube[i])
        p=p.reshape(-1,3)
        p=np.hstack((p,np.ones((p.shape[0],1))))
        p=np.dot(p,T)
        for j in range(0,p.shape[0]):
            if p[j][3]!=0:
                p[j]=p[j]/p[j][3]
            else:
                p[j][0],p[j][1],p[j][2]=550,550,550  
        p=np.delete(p,p.shape[1]-1,1)
        p=list(p.flatten())
        prj.append(p)
    return prj

def init_ppm(cube,d,n,f):
    T=np.zeros((4,4))
    T[0][0],T[0][1],T[0][2] = f[1]*n[1]+f[2]*n[2] , -f[1]*n[0] , -f[2]*n[0]
    T[1][0],T[1][1],T[1][2] = -f[0]*n[1] , f[0]*n[0]+f[2]*n[2] , -f[2]*n[1]
    T[2][0],T[2][1],T[2][2] = -f[0]*n[2] , -f[1]*n[2] , f[0]*n[0]+f[1]*n[1]
    T[3][0],T[3][1],T[3][2] = f[0]*d[0] , f[1]*d[0] , f[2]*d[0]
    T[3][3]= d[1]
    prj=[]
    for i in range(0,6):
        p=np.array(cube[i])
        p=p.reshape(-1,3)
        p=np.hstack((p,np.ones((p.shape[0],1))))
        p=np.dot(p,T)
        for j in range(0,p.shape[0]):
            p[j]=p[j]/p[j][3]
        p=np.delete(p,p.shape[1]-1,1)
        p=list(p.flatten())
        prj.append(p)
    return prj
def parallel(cube,dir,x,n):
    x0,y0,z0 = x[0],x[1],x[2]
    n1,n2,n3 =  n[0],n[1],n[2]
    a,b,c = dir[0],dir[1],dir[2]
    d1=a*n1 + b*n2 + c*n3 
    d0=x0*n1 + y0*n2 + z0*n3    
    prj=init_ppm(cube,[d0,d1],[n1,n2,n3],[a,b,c])
    return prj


def draw_cube(win,cube):
    for i in range(0,6):
        temp=flatten_face(cube[i])
        polygon(temp,win,colors[i])
        #scanfill(temp,win,colors[j])

def unDraw(win,cube,color):
    for i in range(0,6):
        temp=flatten_face(cube[i])
        polygon(temp,win,color)

def flatten_face(face):
    temp=[]
    z=face[2]/sqrt(2)
    for i in range(2,12,3):
        z=face[i]/sqrt(2)
        temp.append(face[i-2]-z)
        temp.append(face[i-1]-z)
    return temp
"""
[[250, 450, 300, 350, 450, 300, 350, 450, 400, 250, 450, 400],
[250 ,350 ,300 ,350 ,350 ,300 ,350 ,350 ,400 ,250 ,350 ,400],
[250 ,450, 300, 250, 350, 300, 250, 350, 400 ,250, 450, 400],
[350 ,450 ,300 ,350 ,450 ,400 ,350 ,350 ,400 ,350 ,350, 300 ],
[250, 450, 400 ,250 ,350 ,400 ,350 ,350, 400 ,350, 450, 400],
[250 ,450 ,300 ,350 ,450 ,300 ,350 ,350 ,300 ,250 ,350, 300]]



 [[0 , 0 , 0 ,400 , 0 , 0 ,400 ,400, 0 , 0, 400, 0],
[0, 0 ,400, 400, 0 ,400, 400, 400, 400, 0 ,400, 400],
[0 ,400 , 0, 0 ,400 ,400 ,400, 400 ,400 ,400 ,400 , 0],
[0, 0, 0, 0, 400 , 0, 0, 400, 400 , 0, 0, 400],
[400, 400, 0, 400, 400, 400, 400, 0, 400, 400, 0, 0],
[0, 0, 0, 0, 0, 400, 400, 0, 400, 400, 0, 0]]




[[0, 0, 0, 100, 0, 0, 100, 100, 0, 0, 100, 0],
[0, 0, 100, 100, 0, 100, 100, 100, 100, 0, 100, 100],
[0, 0, 0, 0, 0, 100, 0, 100, 100, 0, 100, 0],
[100, 0, 0, 100, 0, 100, 100, 100, 100, 100, 100, 0],
[0, 0, 0, 0, 0, 100, 100, 0, 100, 100, 0, 0],
[0, 100, 0, 0, 100, 100, 100, 100, 100, 100, 100, 0]]
"""
