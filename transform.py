def windToView(coords,x,y):
	xwmin=coords[0]
	ywmin=coords[1]
	xwmax=coords[2]
	ywmax=coords[3]
	xvmin=coords[4]
	yvmin=coords[5]
	xvmax=coords[6]
	yvmax=coords[7]
	xView= xvmin+(x-xwmin)*(xvmax-xvmin)//(xwmax-xwmin)
	yView=yvmin+(y-ywmin)*(yvmax-yvmin)//(ywmax-ywmin)
	print(xView,yView)
	return xView,yView

