from tkinter import *

userans=""
def settingsWindowFunc():
    window.withdraw()
    settingsWindow.deiconify()

def functionsWindowFunc():
    window.withdraw()
    functionWindow.deiconify()

def returnToHomeFunc():
    window.deiconify()
    functionWindow.withdraw()
    settingsWindow.withdraw()
    pairWindow.withdraw()

def dataBtnFunc():
    dataBtn.config(text="Data Collection: \n OFF")
    writelabel.config(text="But how will we earn money :( ")

def destructBtnFunc():
    destructBtn.config(text="Disconnected", foreground= "red")
    writelabel.config(text=f"{userans} \n was disconnected! Go to 'Pair' \n to re-connect your microchip")
    status.config(text="Connected to: \n Null (INACTIVE)", background= "red")

def exitFunc():
    exit()

def sightBtnFunc():
    BlindBtn.config(text= "Sight: \n ON", foreground="green")
    writelabel1.config(text= "Wow, you can see now. That's nice")

def deafBtnFunc():
    DeafBtn.config(text= "Hearing: \n ON", foreground="green")
    writelabel1.config(text= "You can hear now, you want a cookie?")

def movementBtnFunc():
    MovementBtn.config(text= "Movement: \n ON", foreground="green")
    writelabel1.config(text="Now you can get off the sofa \n every now and then")

def getPairboxFunc():
    global userans
    userans= pairbox.get()
    writelabel2.config(text=f"'{userans}' \n was succesfully paired!", background="green")
    status.config(text=f"Connected to: \n {userans} (active)", background="green")
    writelabel.config(text="I tell you stuff, occasionally")
    destructBtn.config(text="Disconnect", foreground="green")

def pairWindowFunc():
    pairWindow.deiconify()
    window.withdraw()
    writelabel2.config(text="I tell you stuff, occasionally.", background="gray")

#fenetre un
window= Tk()
window.title("ACA")
settingsBtn= Button(window, text="Settings", command= settingsWindowFunc)
abilitiesBtn= Button(window, text="Functions", command= functionsWindowFunc)
pairBtn= Button(window, text="Pair", command= pairWindowFunc)
name= Label(window, text="Ability Chip App v2.17.0a \n ---------------------------------------")
status= Label(window, text="Connected to: \n Null (INACTIVE)", background="red")
placeholder= Label(window, text= "\n")
placeholder1= Label(window, text="  ")
placeholder1a= Label(window, text="_____________________________________")
exitBtn= Button(window, text="Exit", foreground= "red", command= exitFunc)



#fenetre du settings
settingsWindow= Tk()
settingsWindow.title("ACAS")
writelabel= Label(settingsWindow, text=" I tell you stuff, occasionally.", background="GRAY")
name2= Label(settingsWindow, text="Ability Chip App v2.17.0a \n | SETTINGS | \n --------------------------------------- \n \n")
dataBtn= Button(settingsWindow, text="Data Collection: \n ON", command= dataBtnFunc)
backBtn= Button(settingsWindow, text="Back", command= returnToHomeFunc)
destructBtn= Button(settingsWindow, text= "Disconnected",foreground= "red", command= destructBtnFunc)
placeholder2= Label(settingsWindow, text="  ")
placeholder3= Label(settingsWindow, text="  ")
placeholder4= Label(settingsWindow, text="  ")
placeholder5= Label(settingsWindow, text="_____________________________________")
settingsWindow.withdraw()


#fenetre du functions 
functionWindow= Tk()
functionWindow.title("ACAF")
writelabel1= Label(functionWindow, text=" I tell you stuff, occasionally.", background="GRAY")
name3= Label(functionWindow, text="Ability Chip App v2.17.0a \n | FUNCTIONS | \n --------------------------------------- \n \n")
BlindBtn= Button(functionWindow, text=" Sight: \n OFF", foreground="red", command= sightBtnFunc)
DeafBtn= Button(functionWindow, text= " Hearing: \n OFF", foreground="red", command= deafBtnFunc)
MovementBtn= Button(functionWindow, text= " Movement: \n OFF", foreground="red", command= movementBtnFunc)
backBtn1= Button(functionWindow, text="Back", command= returnToHomeFunc)
placeholder6= Label(functionWindow, text="  ")
placeholder7= Label(functionWindow, text="  ")
placeholder8= Label(functionWindow, text="  ")
placeholder9= Label(functionWindow, text="  ")
placeholder10= Label(functionWindow, text="_____________________________________")
functionWindow.withdraw()

#fenetre du pair
pairWindow= Tk()
pairWindow.title("ACAP")
name4= Label(pairWindow, text="Ability Chip App v2.17.0a \n | PAIRING | \n --------------------------------------- \n \n")
pairbox= Entry(pairWindow, text="Enter the name of your device...")
confirmBtn= Button(pairWindow, text="Confirm", command= getPairboxFunc)
writelabel2=Label(pairWindow, text=" I tell you stuff, occasionally.", background="GRAY")
backBtn2= Button(pairWindow, text="Back", command= returnToHomeFunc)
placeholder11= Label(pairWindow, text="  ")
placeholder12= Label(pairWindow, text="  ")
placeholder13= Label(pairWindow, text="Enter the name of your device...")
pairWindow.withdraw()












#fenetre un de pack
name.grid(row= 0, column= 1)
status.grid(row=1, column=1)
placeholder1.grid(row=2, column=1)
pairBtn.grid(row=3, column=1)
abilitiesBtn.grid(row=4, column=1)
settingsBtn.grid(row=5, column=1)
placeholder.grid(row=6, column=1)
exitBtn.grid(row=7, column=1)
placeholder1a.grid(row=8, column=1)

#fenetre du settings de pack
name2.grid(row=0,column=1)
dataBtn.grid(row=1, column=1)
placeholder2.grid(row=2,column=1)
destructBtn.grid(row=3,column=1)
placeholder3.grid(row=4,column=1)
backBtn.grid(row=5,column=1)
placeholder4.grid(row=6, column=1)
writelabel.grid(row=7, column=1)
placeholder5.grid(row=8,column=1)

#fenetre du function de pack
name3.grid(row=0,column=1)
BlindBtn.grid(row=1,column=1)
placeholder6.grid(row=2,column=1)
DeafBtn.grid(row=3,column=1)
placeholder7.grid(row=4,column=1)
MovementBtn.grid(row=5,column=1)
placeholder8.grid(row=6,column=1)
backBtn1.grid(row=7,column=1)
placeholder9.grid(row=8,column=1)
writelabel1.grid(row=9,column=1)
placeholder10.grid(row=10,column=1)

#fenetre du pair de pack
name4.grid(row=0, column=1)
placeholder13.grid(row=1, column=1)
pairbox.grid(row=2,column=1)
confirmBtn.grid(row=3,column=1)
backBtn2.grid(row=4,column=1)
placeholder11.grid(row=5,column=1)
writelabel2.grid(row=6,column=1)
placeholder12.grid(row=7, column=1)



window.mainloop()
settingsWindow.mainloop()
functionWindow.mainloop()