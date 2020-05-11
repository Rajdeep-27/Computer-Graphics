import numpy as np
from graphics import *
from primitives import *
import math

def create(vertices):
    obj=np.asarray(vertices)
    #print(obj)
    obj=obj.reshape(-1,2)
    #print(obj)
    obj=np.hstack((obj,np.ones((obj.shape[0],1))))
    #print(obj)
    return obj
    
def draw_general(newObj,win,color):
    newObj=newObj/newObj[0][newObj.shape[1]-1]
    newObj=np.delete(newObj,newObj.shape[1]-1,1)
    newObj=list(newObj.flatten())
    for i in range(0,len(newObj),2):
        win.plot(newObj[i],newObj[i+1],color)
    return newObj    

def draw(newObj,win,color):
    newObj=newObj/newObj[0][newObj.shape[1]-1]
    newObj=np.delete(newObj,newObj.shape[1]-1,1)
    newObj=list(newObj.flatten())
    polygon(newObj,win,color)
    return newObj

def translate(vertices,trans,win,color):
    obj=create(vertices)
    tmat=np.identity(3)
    tmat[2][0],tmat[2][1] = -trans[0], -trans[1]
    #print(tmat)
    #print("\n")
    newObj=np.dot(obj,tmat)
    #print(newObj)
    #draw(obj,win,color)
    return draw_general(newObj,win,color)
    

def shear(vertices,shr,win,color):
    obj=create(vertices)
    shmat_x=np.identity(3)
    shmat_y=np.identity(3)
    #print(sh)
    shmat_x[1][0]=shr[0]
    shmat_y[0][1]=shr[1]
    newObj=np.dot(obj,shmat_x)
    newObj=np.dot(newObj,shmat_y)
    #draw(obj,win,color)
    return draw_general(newObj,win,color)

def scale(vertices,fac,point,win,color):
    obj=create(vertices)
    scaleMat=np.identity(3)
    scaleMat[0][0]=fac[0]
    scaleMat[1][1]=fac[1]
    tmat=np.identity(3)
    tmat[2][0],tmat[2][1] = -point[0], -point[1]
    newObj=np.dot(obj,tmat)
    newObj=np.dot(newObj,scaleMat)
    tmat[2][0],tmat[2][1] = point[0], point[1]
    newObj=np.dot(newObj,tmat)
    #draw(obj,win,color)
    return draw_general(newObj,win,color)

def rotate(vertices,rot,angle,win,color):
    obj=create(vertices)
    rot_mat=np.identity(3)
    p=math.pi
    rot_mat[0][0]=rot_mat[1][1]=math.cos(p*angle/180)
    rot_mat[1][0]=-math.sin(p*angle/180)
    rot_mat[0][1]=-rot_mat[1][0]
    tmat=np.identity(3)
    tmat[2][0],tmat[2][1] = -rot[0], -rot[1]
    newObj=np.dot(obj,tmat)
    newObj=np.dot(newObj,rot_mat)
    tmat[2][0],tmat[2][1] = rot[0], rot[1]
    newObj=np.dot(newObj,tmat)
    return draw_general(newObj,win,color)

def reflect(vertices,pm,win,color):
    obj=create(vertices)
    tmat=np.identity(3)
    tmat[2][0],tmat[2][1] = -pm[0], -pm[1]
    newObj=np.dot(obj,tmat)
    if len(pm)==3:
        tan=pm[2]
        angle=math.atan(tan)
        rot_mat=np.identity(3)
        rot_mat[0][0]=rot_mat[1][1]=math.cos(angle)
        rot_mat[1][0]=math.sin(angle)
        rot_mat[0][1]=-rot_mat[1][0]
        newObj=np.dot(newObj,rot_mat)
        ref=np.identity(3)
        ref[1][1]=-1
        newObj=np.dot(newObj,ref)
        rot_mat[1][0],rot_mat[0][1]=rot_mat[0][1],rot_mat[1][0]
        newObj=np.dot(newObj,rot_mat)
    else:        
        ref=np.identity(3)
        ref[0][0]=ref[1][1]=-1
        newObj=np.dot(newObj,ref)
    tmat[2][0],tmat[2][1] = pm[0], pm[1]
    newObj=np.dot(newObj,tmat)
    return draw_general(newObj,win,color)    



        
