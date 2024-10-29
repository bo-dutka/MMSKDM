#encoding: utf-8
from __future__ import division
from nodebox.graphics import *

# Модель польоту снаряду
# dx'/dt=0; dx/dt=x' та dy'/dt=-9.8; dy/dt=y'
def f(xp,yp,x1p,y1p):
    c=0.95
    x1=c*x1p # з рівняння dx'/dt=0
    x=x1*dt+xp # з рівняння dx/dt=x'
    y1=c*(y1p-9.8*dt) # з рівняння dy'/dt=-9.8
    y=y1*dt+yp # з рівняння dy/dt=y'
    return x,y,x1,y1

def draw(canvas):
    global x,y,x1,y1,t,dt,xt,s,x1t
    if canvas.mouse.button==LEFT:
        t,x,y,x1,y1=0,0,0,canvas.mouse.x, canvas.mouse.y # початкові умови
    if x1!=0 and y1!=0:
        if y>=0:
            x,y,x1,y1=f(x,y,x1,y1)
            t+=dt
    canvas.clear()
    fill(0,0,0)
    ellipse(x=x, y=y, width=10, height=10)
    fill(0,100,0)
    rect(x=xt, y=0, width=50, height=20)#корпус
    rect(x=xt+15, y=20, width=25, height=20)#башня
    rect(x=xt+15, y=30, width=-50, height=5)#дуло
    fill(1, 0, 0)
    if x>xt and x<xt+85 and y>0 and y<50:
        s+=1
        x,y,x1,y1=0,0,0,0
        xt=700
        x1t-=0.1
    if xt<0:
        text("Game Failed",280,250)
    xt+=x1t
    text("Score: " + str(s),300,300)
x,y,x1,y1=0,0,0,0
dt=0.1
t=0
xt=700
x1t=-2.5
s=0
canvas.size = 800, 500
canvas.run(draw)