def compute_outcode(x,y,xmin,ymin,xmax,ymax):
    left=1
    right=2
    bottom=4    
    top=8

    outcode=0
    if y>ymax:
        outcode|=top
    elif y<ymin:
        outcode|=bottom
    if x>xmax:
        outcode|=right
    elif x<xmin:
        outcode|=left
    return outcode

def clip_line(win,coords, clip_win):

    xmin = min(clip_win[0],clip_win[2],clip_win[4],clip_win[6])
    ymin = min(clip_win[1],clip_win[3],clip_win[5],clip_win[7])
    xmax = max(clip_win[0],clip_win[2],clip_win[4],clip_win[6])
    ymax = max(clip_win[1],clip_win[3],clip_win[5],clip_win[7])
    x0,y0,x1,y1=coords[0],coords[1],coords[2],coords[3]
    left=1
    right=2
    bottom=4    
    top=8
    out_1 = compute_outcode(x0, y0, xmin, ymin, xmax, ymax)
    out_2 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)    
    accept = False
    done = False    
    while done!=True:    
        x = 0
        y = 0    
        if out_1==0 and out_2==0:
            print("Accepted")
            accept = True
            done = True
            break
        if out_1 & out_2:
            accept = False
            done = True
            break            
        outcode = 0        
        if out_1 != 0:
            outcode = out_1
        else:
            outcode = out_2            
        if outcode & top:
            x = (ymax - y0) * (x1 - x0)/(float)(y1- y0) + x0
            y = ymax
        elif outcode & bottom:
            x = (ymin - y0) * (x1 - x0)/(float)(y1- y0) + x0
            y = ymin
        elif outcode & right:
            y = (xmax - x0) * (y1 - y0)/(float)(x1 - x0) + y0
            x = xmax
        elif outcode & left:
            y = (xmin - x0) * (y1 - y0)/(float)(x1 - x0) + y0
            x = xmin            
        if outcode == out_1:
            x0 = x
            y0 = y
            out_1 = compute_outcode(x0, y0, xmin, ymin, xmax, ymax)
        else:
            x1 = x
            y1 = y
            out_2 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)                   
    if accept:
        print("Line Accepted from ", x0, y0, x1, y1)
        return [x0,y0,x1,y1]        
    else:
        print("Line not accpted")

from graphics import *
from bresenham import *
wincords=list(map(int,input("Window Coordinates=> ").split()))
win=GraphWin("Window",800,800)
win.setCoords(wincords[0], wincords[1], wincords[2], wincords[3])
bresenham([wincords[0], 0, wincords[2], 0],win,'red')
bresenham([0, wincords[1], 0, wincords[3]],win,'blue')
clip_win = list(map(int, input("Clipping window coordinates(counterclockwise order)=> ").split()))
polygon(clip_win,win,'black')
i='j'
while(i!='x'):
    coords=list(map(int,input("End points of line=> ").split()))
    bresenham(coords,win,'black')
    clipped=clip_line(win,coords,clip_win)
    bresenham(clipped,win,'green')
    i=input("Press x to exit\nPress any other key to continue\n")
win.getMouse()
win.close()    