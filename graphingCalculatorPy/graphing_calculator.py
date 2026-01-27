from turtle import *
from math import *
from tkinter import *
my = int(input("How tall do you want the graph? (multiples of 10 only)\t"))
mx = int(input("How long do you want the graph? (multiples of 10 only)\t"))
z=str(input("Animate the graph?\t"))
k=float(input("Intervals of x (graph is more detailed at lower values, but animation time increased)? \t"))
if z.strip().lower()== "yes":
    d=1
else:
    d=0
print('Note that 5(x) or 5x will not work. You must use 5*x or 5*(x) for this application to work')
hi=str(input("Press any key to continue"))
graph = Screen()
hideturtle()
graph.setup(mx, my)
user_input = int(textinput("Config Window", "How many graphs will you plot?"))
graphs,gc=[],[]

for i in range(user_input):
    r= textinput(f"Config Window" , f"Graph {i+1}\n f(x)= ")
    graphs.append(r)
    p= textinput(f"Config Window", f"Graph {i+1}'s colour?")
    gc.append(p)

def drawAxis():
    graph.tracer(0)
    speed(0)
    penup()
    goto(0, my//2)   # start at top center
    seth(270)        # face straight down
    pendown()

    for i in range(0, my, 10):  # draw y axis
        pendown()
        forward(10)
        seth(180),forward(5),penup(), forward(2),seth(-90),backward(8), write(my//2-i, align="right", font=("Arial", 4, "normal")),forward(8),seth(180), backward(2),pendown(), backward(10),forward(5),seth(270)
    penup()
    goto(-(mx//2),0)
    pendown()
    for i in range(0,mx,10):  # draw x axis
        seth(0)
        forward(10)
        seth(-90),forward(5),penup(), forward(2),seth(90),backward(8), write(-mx//2+i+10, align="center", font=("Arial", 4, "normal")),forward(8),seth(-90), backward(2),pendown(), backward(10),forward(5),seth(0)
    graph.update()
    graph.tracer(1)

def graphPlot(c,e):
    global k
    graph.tracer(d)
    pencolor(c)
    penup()
    """for t in range(-(mx//2), mx//2, 1):
        x=t
        y=eval(e)
        goto(x,y)
        pendown()"""
    i=-(mx/2)
    while i < (mx/2):
        x=i
        y=eval(e)
        goto(x,y)
        pendown()
        i+=k
        
drawAxis()

penup()
for i in range(len(graphs)):
    penup()
    goto(-400, 400-(i*20))
    pendown()
    pencolor(gc[i])
    write(f"Graph {i+1}: {graphs[i]}")
for i in range(len(graphs)):
    graphPlot(gc[i],graphs[i])
done()
