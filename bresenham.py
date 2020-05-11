def bresenham(coord,window,color):
	if coord[0]>coord[2]:
		coord[0],coord[2]=coord[2],coord[0]
		coord[1],coord[3]=coord[3],coord[1]
	xi=coord[0]
	yi=coord[1]
	xf=coord[2]
	yf=coord[3]
	a=yf-yi
	b=xi-xf
	if b==0:
		yf=max(yf,yi)
		yi=coord[1]+coord[3]-yf
		while yi<=yf:
			#print(xi,yi)
			window.plot(xi,yi,color)
			yi+=1
	else:			
		m=(yf-yi)/(xf-xi)
		if m==0:
			while xi<=xf:
				#print(xi,yi)
				window.plot(xi,yi,color)
				xi+=1
		elif m>0 and m<=1:
			d=2*a+b
			while(xi<=xf):
				if d<0:
					d+=2*a
				else:
					d+=2*(a+b)
					yi+=1
				xi+=1
				#print(xi,yi)
				window.plot(xi,yi,color)				
		elif m>1:
			d=a+2*b
			while yi<=yf:
				if d>0:
					d+=2*b
				else:
					xi+=1
					d+=2*(a+b)
				yi+=1
				#print(xi,yi)
				window.plot(xi,yi,color)
		elif m<=-1:
			d=a-2*b
			while yi>yf:
				if d<0:
					d-=2*b
				else:
					xi+=1
					d+=2*(a-b)	
				yi-=1
				#print(xi,yi)
				window.plot(xi,yi,color)
		else :
			d=2*a-b
			while xi<=xf:
				if d>0:
					d+=2*a
				else:
					yi-=1
					d+=2*(a-b)
				xi+=1
				#print(xi,yi)
				window.plot(xi,yi,color)										
def polygon(vertices,window,color):
	m=len(vertices)
	for i in range(0,len(vertices),2):
		bresenham([vertices[i%m],vertices[(i+1)%m],vertices[(i+2)%m],vertices[(i+3)%m]],window,color)

def plotAxes(win,points,color):
	bresenham([points[0],0,points[2],0],win,color)
	bresenham([0,points[1],0,points[3]],win,color)
