def circle(h,k,r,win):
	d=1-r #assuming r is integer only else d=5/4 -r
	x=0
	y=r
	while x<y:
		if d>0:
			d+=2*(x-y)+5
			y=y-1
		else:
			d+=2*x+3
		x=x+1
		win.plot(x+h,y+k,'red')
		win.plot(y+h,x+k,'red')
		win.plot(y+h,k-x,'red')
		win.plot(x+h,k-y,'red')
		win.plot(h-x,k-y,'red')
		win.plot(h-y,k-x,'red')
		win.plot(h-y,x+k,'red')
		win.plot(h-x,y+k,'red')
		print(x+h,y+k)
from graphics import *
from transform import *
from bresenham import *
points=list(map(int,input("Window Coordinates=> ").split()))
window=GraphWin("Window",400,400)
window.setCoords(points[0],points[1],points[2],points[3])
ends=[0,points[1],0,points[3]]
bresenham(ends,window)
ends=[points[0],0,points[2],0]
bresenham(ends,window)
view=GraphWin("Viewport",800,800)
view.setCoords(-800,-800,800,800)
points.extend([-800,-800,800,800])
ends=[0,points[5],0,points[7]]
bresenham(ends,view)
ends=[points[4],0,points[6],0]
bresenham(ends,view)
#print(points)
coord=list(map(int,input("Center and radius=> ").split()))
r=coord[2]
a,b=windToView(points,0,0)
c,d=windToView(points,r,0)
R=abs(a-c)
print( R)
circle(coord[0],coord[1],r,window)
xv,yv=windToView(points,coord[0],coord[1])
circle(xv,yv,R,view)
input("Press x to exit=> ")
