def putPixel(win,x,y,h,k):
	win.plot(x+h,y+k)
	win.plot(x+h,k-y)
	win.plot(h-x,y+k)
	win.plot(h-x,k-y)
def ellipse(win,cen,alx,aly):
	h=cen[0]
	k=cen[1]
	b=abs(aly[1]-aly[3])//2
	a=abs(alx[0]-alx[2])//2
	x=0
	y=b
	d=(a**2)*(1-4*y)+4*(b**2)*(2*x+1)
	while abs((b**2)*x)<abs((a**2)*y):
		if d>0:#SE			
			d+=4*(b**2)*(3+2*x)	+4*(a**2)*(2-2*y)
			y-=1		
		else: #E
			d+=4*(b**2)*(3+2*x)
		x+=1
		putPixel(win,x,y,h,k)
		print(x+h,y+k)
	d=(b**2)*(4*x+1)+4*(a**2)*(1-2*y)	
	while y>=0:		
		if d>0:#S
			d+=4*(a**2)*(-2*y+3)			
		else:
			d+=4*((b**2)*(2+2*x))+4*(a**2)*(-2*y+3)
			x+=1
		y-=1
		putPixel(win,x,y,h,k)
		print(x+h,y+k)		
from graphics import *
from transform import *
from bresenham import *
wind=list(map(int,input("Window coordinates=> ").split()))
view=list(map(int,input("Device coordinates=> ").split()))
cen=list(map(int,input("Centre coordinates=> ").split()))
alx=list(map(int,input("Axes coordinates aligned to x=> ").split()))
aly=list(map(int,input("Axes coordinates aligned to y=> ").split()))
window=GraphWin("Window",1000,1000)
window.setCoords(wind[0],wind[1],wind[2],wind[3])
viewPort=GraphWin("ViewPort",500,500)
viewPort.setCoords(view[0],view[1],view[2],view[3])
ends=[0,wind[3],0,wind[1]]
bresenham(ends,window)
ends=[wind[0],0,wind[2],0]
bresenham(ends,window)
ends=[0,view[3],0,view[1]]
bresenham(ends,viewPort)
ends=[view[0],0,view[2],0]
bresenham(ends,viewPort)
points=wind+view
cview=[0,0]
cview[0],cview[1]=windToView(points,cen[0],cen[1])
xv=[0,0,0,0]
xv[0],xv[1]=windToView(points,alx[0],alx[1])
xv[2],xv[3]=windToView(points,alx[2],alx[3])
yv=[0,0,0,0]
yv[0],yv[1]=windToView(points,aly[0],aly[1])
yv[2],yv[3]=windToView(points,aly[2],aly[3])
ellipse(window,cen,alx,aly)
ellipse(viewPort,cview,xv,yv)
input("Press to exit=> ")

