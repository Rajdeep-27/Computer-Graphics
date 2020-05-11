def dict_to_list(dic):
	dic=dic.keys()
	dic=[i for j in dic for i in j]
	return dic
def bresenham(coord,window,color):
	vertices={}
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
			vertices[(xi,yi)]=1
			yi+=1
	else:			
		m=(yf-yi)/(xf-xi)
		if m==0:
			while xi<=xf:
				#print(xi,yi)
				window.plot(xi,yi,color)
				vertices[(xi,yi)]=1
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
				vertices[(xi,yi)]=1				
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
				vertices[(xi,yi)]=1
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
				vertices[(xi,yi)]=1
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
				vertices[(xi,yi)]=1
	return vertices		
														
def polygon(vertices,window,color):
	m=len(vertices)
	points={}
	for i in range(0,len(vertices),2):
		a=bresenham([vertices[i%m],vertices[(i+1)%m],vertices[(i+2)%m],vertices[(i+3)%m]],window,color)
		if a is not None:
			points.update(a)
	return points	

def plotAxes(win,points,color):
	bresenham([points[0],0,points[2],0],win,color)
	bresenham([0,points[1],0,points[3]],win,color)

def circle(h,k,r,win,color):
	vertices={}
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
		win.plot(x+h,y+k,color)
		win.plot(y+h,x+k,color)
		win.plot(y+h,k-x,color)
		win.plot(x+h,k-y,color)
		win.plot(h-x,k-y,color)
		win.plot(h-y,k-x,color)
		win.plot(h-y,x+k,color)
		win.plot(h-x,y+k,color)
		vertices[(x+h,y+k)]=1
		vertices[(y+h,x+k)]=1
		vertices[(y+h,k-x)]=1
		vertices[(x+h,k-y)]=1
		vertices[(h-x,k-y)]=1
		vertices[(h-y,k-x)]=1
		vertices[(h-y,x+k)]=1
		vertices[(h-x,y+k)]=1
		print(x+h,y+k)
	return vertices
		
def putPixel(win,x,y,h,k):
	vertices={}
	win.plot(x+h,y+k)
	win.plot(x+h,k-y)
	win.plot(h-x,y+k)
	win.plot(h-x,k-y)
	vertices[(x+h,y+k)]=1
	vertices[(x+h,k-y)]=1
	vertices[(h-x,y+k)]=1
	vertices[(h-x,k-y)]=1
	return vertices
def ellipse(win,cen,alx,aly):
	vertices={}
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
		vertices.update(putPixel(win,x,y,h,k))
		print(x+h,y+k)
	d=(b**2)*(4*x+1)+4*(a**2)*(1-2*y)	
	while y>=0:		
		if d>0:#S
			d+=4*(a**2)*(-2*y+3)			
		else:
			d+=4*((b**2)*(2+2*x))+4*(a**2)*(-2*y+3)
			x+=1
		y-=1
		vertices.update(putPixel(win,x,y,h,k))
		print(x+h,y+k)
	return vertices		

def undraw(vertices,win,color):
	for i in range(0,len(vertices),2):
			win.plot(vertices[i],vertices[i+1],color)

def plot3Daxes(win,points,color):
	mp=[]
	mp.append((points[0]+points[2])/2)
	mp.append((points[1]+points[3])/2)
	bresenham([mp[0],mp[1],mp[0],points[3]/2],win,color)
	bresenham([mp[0],mp[1],points[2]/2,mp[1]],win,color)
	x=(points[0]+mp[0])/3
	y=(points[1]+mp[1])/3
	bresenham([mp[0],mp[1],x,y],win,color)