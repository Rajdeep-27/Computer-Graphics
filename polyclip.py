from graphics import *
from bresenham import *
from fill import *
def intersect(edge,line):
    inter=[]
    if edge[0]!=edge[2] and edge[1]!=edge[3]:
        c=(edge[1]*edge[2]-edge[3]*edge[0])/(edge[2]-edge[0])
        m=(edge[3]-edge[1])/(edge[2]-edge[0])
        #inter=[]
        if line[0]==line[2]:
            inter.append(line[0])
            inter.append(m*line[0]+c)
        elif line[1]==line[3]:
            inter.append((line[1]-c)/m)
            inter.append(line[1])
        return inter
    elif edge[0]==edge[2] and edge[1]!=edge[3]:
        if(line[1]==line[3]):
            inter=[edge[0],line[1]]
        elif(line[0]==line[2]):
            if(line[0]-edge[0])*(line[0]-edge[2])<=0:
                inter=[line[0],line[1]]    
            else:
                inter=[line[2],line[3]]  
    elif edge[0]!=edge[2] and edge[1]==edge[3]:
        if(line[0]==line[2]):
            inter=[line[0],edge[1]]
        elif(line[1]==line[3]):
            if(line[1]-edge[1])*(line[1]-edge[3])<=0:
                inter=[line[0],line[1]]   
            else:
                inter=[line[2],line[3]]  
    return inter 
def clip(ex,vertices,ends,win):
    n=len(ends)
    for i in range(0,len(ends),2):
        m=len(vertices)
        aux=[]
        for j in range(0,len(vertices),2):
            print(i,j)
            if ends[(i+1)%n]==ends[(i+3)%n]:
                if(ends[(i+1)%n]==ex[3]):
                    if(vertices[(j+1)%m]>ex[3]): a=0
                    else: a=1
                    if(vertices[(j+3)%m]>ex[3]): b=0
                    else: b=1
                elif(ends[(i+1)%n]==ex[2]):
                    if(vertices[(j+1)%m]>=ex[2]): a=1
                    else: a=0
                    if(vertices[(j+3)%m]>=ex[2]): b=1
                    else: b=0
            else:
                if(ends[i%n]==ex[1]):
                    if(vertices[(j)%m]>ex[1]): a=0
                    else: a=1
                    if(vertices[(j+2)%m]>ex[1]): b=0
                    else: b=1
                elif(ends[i%n]==ex[0]):
                    if(vertices[(j)%m]>=ex[0]): a=1
                    else: a=0
                    if(vertices[(j+2)%m]>=ex[0]): b=1
                    else: b=0                   
            print(a,b,ends[i%n],ends[(i+1)%n],ends[(i+2)%n],ends[(i+3)%n])
            print(vertices[j%m],vertices[(j+1)%m],vertices[(j+2)%m],vertices[(j+3)%m])
            if a+b==1:
                edge=[]
                line=[]
                for k in range (0,4,1):
                    edge.append(vertices[(j+k)%m])
                for k in range (0,4,1):
                    line.append(ends[(i+k)%n])   
                inter=intersect(edge,line)
                print(inter)                
                if a==1 and b==0:
                    aux.extend(inter)
                    #vertices[(j+2)%m],vertices[(j+3)%m]=inter[0],inter[1]
                if a==0 and b==1:
                    aux.extend(inter)
                    aux+=[vertices[(j+2)%m],vertices[(j+3)%m]]
            elif a+b==2:
                aux+=[vertices[(j+2)%m],vertices[(j+3)%m]]
        vertices=aux
        print(vertices)                    
    return vertices
points=list(map(int,input("Window Coordinates: ").split()))
win=GraphWin("window",800,800)
win.setCoords(points[0],points[1],points[2],points[3])
ends=list(map(int,input("Clipping window vertices(counter clockwise): ").split()))
vertices=list(map(int,input("Polygon vertices in counter clockwise order: ").split()))
polygon(ends,win,"black")
polygon(vertices,win,"red")
xmin=min([ends[0],ends[2],ends[4],ends[6]])
xmax=max([ends[0],ends[2],ends[4],ends[6]])
ymin=min([ends[1],ends[3],ends[5],ends[7]])
ymax=max([ends[1],ends[3],ends[5],ends[7]])
ex=[xmin,xmax,ymin,ymax]
print(ex)
clipped=clip(ex,vertices,ends,win)
polygon(clipped,win,'green')
scanfill(clipped,win,'purple')
win.getMouse()
#sample input
#Window Coordinates: -200 -200 200 200
#Clipping window vertices(counter clockwise): 75 75 75 -75 -75 -75 -75 75
#Polygon vertices in counter clockwise order: 100 100 55 10 85 0 55 -10 100 -100 10 -55 0 -85 -10 -55 -100 -100 -55 -10 -85 0 -55 10 -100 100 -10 55 0 85 10 55

