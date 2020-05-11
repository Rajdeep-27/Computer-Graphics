from graphics import *
from bresenham import *
coords=list(map(int,input("Window coordinates=> ").split()))
win=GraphWin("Polygon",500,500)
win.setCoords(coords[0],coords[1],coords[2],coords[3])
vertices=list(map(int,input("Enter the vertices in counterclockwise direction=> ").split()))
m=len(vertices)
for i in range(0,m,2):
	points=[vertices[i%m],vertices[(i+1)%m],vertices[(i+2)%m],vertices[(i+3)%m]]
	print(points)
	bresenham(points,win)
input("Press x to exit=> ")	

