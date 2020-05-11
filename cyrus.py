def cyrus(ends,points):
	normals=[[-1,0],[0,1],[1,0],[0,-1]]
	x0,y0,x1,y1=ends[0],ends[1],ends[2],ends[3]
	index=0
	te=[]
	tl=[]
	TE,TL=0,1
	for n in normals:
		p=points[index]
		index+=1
		nume=(x0-p[0])*n[0]+(y0-p[1])*n[1]
		deno=(x1-x0)*n[0]+(y1-y0)*n[1]
		if deno<0:
			te.append(-nume/deno)
		elif deno>0:
			tl.append(-nume/deno)	
	if(max(te)<min(tl)):
		TE=max(TE,max(te))
		TL=min(TL,min(tl))
	xe,ye=x0+(x1-x0)*TE,y0+(y1-y0)*TE
	xl,yl=x0+(x1-x0)*TL,y0+(y1-y0)*TL
	return [xe,ye,xl,yl]
	
def reorder(points):
	xmin=min(points[0],points[2],points[4],points[6])
	ymin=min(points[1],points[3],points[5],points[7])
	xmax=max(points[0],points[2],points[4],points[6])
	ymax=max(points[1],points[3],points[5],points[7])
	return [[xmin,ymin],[xmin,ymax],[xmax,ymax],[xmax,ymin]]
				
from graphics import *
from bresenham import *

points=list(map(int,input("Window coordinates=> ").split()))
win=GraphWin("clipping",800,800)
win.setCoords(points[0],points[1],points[2],points[3])
points=list(map(int,input("Clipping window vertices=>  ").split()))
points=reorder(points)
m=len(points)
for i in range(m):
	coords=[points[i%m][0],points[i%m][1],points[(i+1)%m][0],points[(i+1)%m][1]]
	bresenham(coords,win,'green')
i='q'	
while i!='x':
	ends=list(map(int,input("End points of line=> ").split()))
	bresenham(ends,win,'red')
	cp=cyrus(ends,points)
	bresenham(cp,win,'black')
	i=input("press x to exit: ")
			




 

