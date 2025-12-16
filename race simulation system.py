from tkinter import *
from tkinter import ttk
from turtle import *  
from turtle import RawTurtle, TurtleScreen
root=Tk()
root.title("RACE SIMULATION SYSTEM (RSS)")


turtleCanvas = Canvas(root, width=200, height=200,bg="grey")
turtleCanvas1 = Canvas(root, width=200, height=200, bg='grey')
turtleCanvas.grid(row=0, column=1, rowspan=6, padx=5)
turtleCanvas1.grid(row=0, column=1, rowspan=6,columnspan=2,sticky="se",padx=80)
dtScreen = TurtleScreen(turtleCanvas)
dtScreen.bgcolor('#F0F0F0')
vtScreen = TurtleScreen(turtleCanvas1)
vtScreen.bgcolor('#F0F0F0')


speeds=[1,0]
distances=[1,0]
times=[]
coolTable=ttk.Treeview(root,columns=("1","2","3"),show="headings")
coolTable.heading("1",text="Times (ms)")
coolTable.heading("2",text="Distances (m)")
coolTable.heading("3",text="Velocities (m/s)")

def calcDrag(fArea,cDrag,speed):
    return (1/2)*1.225*(fArea)*(cDrag)*(speed**2)+0.037# air res and wheel friction
    

def findSpeedWhilePowered(fArea,cDrag,mass,timePowered):
    global speeds, distances, pointOfReversal, times
    i=0
    forwardForce=0
    netforce=0
    distance=0
    speed=0
    speeds=[]
    distances=[]
    times=[]
    pointOfReversal=-1
    while i <= timePowered:
        forwardForce=forceAtTime(i)
        netforce= forwardForce-calcDrag(fArea,cDrag,speed)
        acc= netforce/(mass/1000)
        speed += acc*0.001
        distance+=speed*0.001
        speeds.append(speed)
        distances.append(distance)
        times.append(i)
        try:
            if speeds[i-1] > speed and pointOfReversal==-1:
                pointOfReversal=i
        except:
            pass
        i+=1
    return 0 

def forceAtTime(ms):
    burn_duration = 650  # ms
    max_force = 2.87     # N

    if ms < 0:
        return 0
    elif ms <= burn_duration:
        return max_force * (1 - ms / burn_duration)
    else:
        return 0


def findSpeedWhileCoast(mass,fArea,cDrag,distanceOfTrack):
    global speeds, distances, pointOfReversal, times
    lastSpeed=speeds[-1]
    netforce=0
    speed=lastSpeed
    distance=distances[-1]
    i= len(speeds)
    done=False
    while True:
        netforce=-calcDrag(fArea,cDrag,speed)
        acc=netforce/(mass/1000)
        speed+=acc*0.001
        if speed <=0:
            done=True
        distance+=speed*0.001
        if distance>=distanceOfTrack:
            done=True
        speeds.append(speed)
        distances.append(distance)
        times.append(i)
        try:
            if speeds[i-1] > speed and pointOfReversal==-1:
                pointOfReversal=i
        except:
            pass
        if done:
            break
        i+=1
    coolTable.delete(*coolTable.get_children())

    coolTable.tag_configure("highlight", background="#ffb3b3")
    for i in range(0,len(speeds),50):
        print(f"At {i} milliseconds: speed={speeds[i]:.2f} M/S")
        coolTable.insert("","end",values=(f"{i} milliseconds",f"{distances[i]:.2f} meters (+{distances[i]-distances[i-1]:.3f}m)",f"{speeds[i]:.2f} m/s  ({'+' if speeds[i]>  speeds[i-1] else ''}{speeds[i]-speeds[i-1]:.3f}m/s)"),tags=('highlight',) if speeds[i] < speeds[i-1] and times[i] != 0 else '')
        coolTable.tag_configure("highlight", background="#ffb3b3")



    print("\n\n\n\n\n")
    for i in range(0,len(distances),50):
        print(f"At {i} milliseconds: distance={distances[i]:.2f} M")
    print(f"\n\nThe car took {len(distances)} milliseconds to complete the track. \nIt's max speed was {max(speeds):.2f} M/S and it's final speed was {speeds[-1]:.2f} M/S")
    print(f"The car stopped accelerating at {pointOfReversal} milliseconds.")


def setVals():
    try:
        mass=float(massEntry.get())
        fArea=float(fAreaEntry.get())
        cDrag=float(cDragEntry.get())
        timePowered=float(timePoweredEntry.get())
        trackDistance=float(trackDistanceEntry.get())
        

    except ValueError:
        btn.config(fg="red")
        if any(entry.get().strip() == "" for entry in (massEntry, fAreaEntry, cDragEntry, timePoweredEntry, trackDistanceEntry)):
            btn.config(text="RUN SIMULATION WITH CURRENT SETTINGS\n[STATUS: FAILED (NULL_TYPE_ERROR)]")
        else:
            btn.config(text="RUN SIMULATION WITH CURRENT SETTINGS\n[STATUS: FAILED (INVALID_TYPE_ERROR)]")
        return


    try:
        findSpeedWhilePowered(fArea,cDrag,mass,timePowered)
        findSpeedWhileCoast(mass,fArea,cDrag,trackDistance)
        btn.config(text="RUN SIMULATION WITH CURRENT SETTINGS\n[STATUS: SUCCEEDED]",fg="green")
        drawGraphToTurtle(dtScreen,distances,times, "s", "m","DISTANCE-TIME")
        drawGraphToTurtle(vtScreen,speeds,times, "s", "m/s","VELOCITY-TIME")
        resultsLabel.config(text=f"RESULTS:\n\nPOINT OF DECELERATION- {pointOfReversal:.2f}ms\nMAX ACHIEVED VELOCITY- {max(speeds):.2f}m/s\nFINAL VELOCITY- {speeds[-1]:.2f}m/s\nTIME TO COMPLETE- {len(times)}ms")
        return
    except Exception as e:
        btn.config(text=f"RUN SIMULATION WITH CURRENT SETTINGS\n[STATUS: FAILED ({(type(e).__name__).upper()})",fg='red')
        return


thing=[]

btn=Button(root,text="RUN SIMULATION WITH CURRENT SETTINGS\n[STATUS: N/A]",background='black',fg="white",command=setVals)

thing.append(Label(root,text="Mass (grams):"))

thing.append(Label(root,text="Frontal area (m^2):"))
thing.append(Label(root,text="Drag co-efficient(C-d):"))
thing.append(Label(root,text="Burn duration (ms):"))
thing.append(Label(root,text="Track length (meters):"))

resultsLabel=Label(root,text="RESULTS:\n\nPOINT OF DECELERATION- N/A\nMAX ACHIEVED VELOCITY- N/A\nFINAL VELOCITY- N/A\nTIME TO COMPLETE- N/A")

massEntry=Entry(root)
massEntry.config(width=8)
fAreaEntry=Entry(root)
fAreaEntry.config(width=8)
cDragEntry=Entry(root)
cDragEntry.config(width=8)
timePoweredEntry=Entry(root)
timePoweredEntry.config(width=8)
trackDistanceEntry=Entry(root)
trackDistanceEntry.config(width=8)

def drawGraphToTurtle(tWindow,indepVar,depVar,unitX,unitY,graphName):
    global pointOfReversal
    #   draw axis
    tWindow.clear()
    t=RawTurtle(tWindow)
    tWindow.bgcolor('#F0F0F0')
    tWindow.tracer(False)
   
    
    t.ht()
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    t.goto(-100,100)
    t.goto(-100,-99)
    t.goto(100,-99)
    t.penup()
    #   draw axis labels at max
    mX=max(depVar)
    mY=max(indepVar)
    
    t.goto(-95,87)
    t.write(f"{mY:.2f}{unitY}\t{graphName}")
    t.goto(70,-98)
    t.write(f"{mX:.0f}{unitX}")
    scaleX=200/ mX
    scaleY=200/ mY
    t.color('blue')
    #draw graph
    for i in range(len(depVar)):
        
        t.goto(depVar[i]*scaleX -100,indepVar[i]*scaleY -100)
        t.pendown()
    t.penup()



           


for i in range(len(thing)):
    thing[i].grid(row=i+1,column=0,sticky="e")



massEntry.grid(row=1,column=1,sticky="w")  
fAreaEntry.grid(row=2,column=1,sticky="w")
cDragEntry.grid(row=3,column=1,sticky="w")
timePoweredEntry.grid(row=4,column=1,sticky="w")
trackDistanceEntry.grid(row=5,column=1,sticky="w")
btn.grid(row=6,column=0,sticky='nsew',columnspan='2')
root.rowconfigure(7, weight=1)
root.columnconfigure(1, weight=1)
coolTable.grid(row=7,column=0,columnspan=2,sticky="nsew")
resultsLabel.grid(row=7,column=2,sticky="w")



root.mainloop()


        



