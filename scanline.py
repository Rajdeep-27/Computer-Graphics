import math
def scanfill(edge_table,ymin,ymax,win):
    active=[]
    #active+=edge_table[0]
    curr_y=0
    print(active)
    while  curr_y+ymin<ymax:
        print(curr_y+ymin)
        i=0
        while i<len(active):
            if(active[i][2]==curr_y+ymin):
                del(active[i])
                i-=1
            i+=1  
        for i in range(0,len(active),1):
            if(i%2==0):
                active[i][0]+=active[i][3]
                active[i][1]=math.ceil(active[i][0])
            else:
                active[i][0]+=active[i][3]
                active[i][1]=math.floor(active[i][0])            
        if(len(edge_table[curr_y])):
            active+=edge_table[curr_y]        
            print(active)
        active=sorted(active,key=lambda x:x[1])
        for i in range(0,len(active),2):
            x0=active[i][1]
            xf=active[i+1][1]
            print(x0,xf)
            while(x0<=xf):
                win.plot(x0,curr_y+ymin,'red')
                x0+=1               
        print(curr_y)    
        print(active) 
        curr_y+=1
from graphics import *
from bresenham import *
points=list(map(int,input("Window coordinates=> ").split()))
win=GraphWin("Window",800,800)
win.setCoords(points[0],points[1],points[2],points[3])
coord=[0,points[1],0,points[3]]
bresenham(coord,win,'black')
coord=[points[0],0,points[2],0]
bresenham(coord,win,'black')
#while inp!='x':
vertices=list(map(int,input("Enter vertices in counterclockwise order=> ").split()))
ymin=vertices[1]
ymax=vertices[1]
for i in range(1,len(vertices),2):
    ymin=min(ymin,vertices[i])
    ymax=max(ymax,vertices[i])
for i in range(0,len(vertices),2):
    xmin=min(ymin,vertices[i])
    xmax=max(ymax,vertices[i])    
if(xmax!=xmin and ymax!=ymin):
    s=len(vertices)
    edge_table=[[] for i in range(0,ymax-ymin+1)]
    for i in range(0,len(vertices),2):
        y=vertices[(i+1)%s]+vertices[(i+3)%s]
        if(vertices[(i+1)%s]<vertices[(i+3)%s]):
            if(vertices[i%s]==vertices[(i+2)%s]): m=0
            else:
                m=(vertices[i%s]-vertices[(i+2)%s])/(vertices[(i+1)%s]-vertices[(i+3)%s])
            edge_table[vertices[(i+1)%s]-ymin].append([vertices[i%s],vertices[i%s],vertices[(i+3)%s],m])
        elif(vertices[(i+1)%s]>vertices[(i+3)%s]):
            if(vertices[i%s]==vertices[(i+2)%s]): m=0
            else:
                m=(vertices[i%s]-vertices[(i+2)%s])/(vertices[(i+1)%s]-vertices[(i+3)%s])
            edge_table[vertices[(i+3)%s]-ymin].append([vertices[(i+2)%s],vertices[(i+2)%s],vertices[(i+1)%s],m])
    print(edge_table)
    scanfill(edge_table,ymin,ymax,win)
input("Press x to exit=> ")    