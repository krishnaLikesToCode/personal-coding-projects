import tkinter as tk#i know the code is very in-efficent, i made this in y7 and i honestly can't be bothered to fix it. bite me
import random
import time
mainwindow = tk.Tk()
mainwindow.title("Noughts and crosses")
isPlayerTurn = True 
writeLabel= tk.Label(text= "Let's play!")



def buttonPress1():
    global isPlayerTurn
    if btn1.cget("text") == " O " or btn1.cget("text") == " X ":

        writeLabel.config(text="Don't select an already selected box!")
    else:
        btn1.config(background= 'blue', text= " X ")
        isPlayerTurn = False  
        aiMove()


def buttonPress2():
    global isPlayerTurn
    if btn2.cget("text") == " O " or btn2.cget("text") == " X ":

        writeLabel.config(text="Don't select an already selected box")
    else:
        btn2.config(background= 'blue', text= " X ")
        isPlayerTurn = False  
        aiMove()


def buttonPress3():
    global isPlayerTurn
    if btn3.cget("text") == " O " or btn3.cget("text") == " X ":

        writeLabel.config(text="Don't select an already selected box")
    else:
        btn3.config(background= 'blue', text= " X ")
        isPlayerTurn = False
        aiMove()


def buttonPress4():
    global isPlayerTurn
    if btn4.cget("text") == " O " or btn4.cget("text") == " X ":
   
        writeLabel.config(text="Don't select an already selected box")
    else:
        btn4.config(background= 'blue', text= " X ")
        isPlayerTurn = False
        aiMove()


def buttonPress5():
    global isPlayerTurn
    if btn5.cget("text") == " O " or btn5.cget("text") == " X ":

        writeLabel.config(text="Don't select an already selected box")
    else:
        btn5.config(background= 'blue', text= " X ")
        isPlayerTurn = False
        aiMove()


def buttonPress6():
    global isPlayerTurn
    if btn6.cget("text") == " O " or btn6.cget("text") == " X ":

        writeLabel.config(text="Don't select an already selected box")
    else:
        btn6.config(background= 'blue', text= " X ")
        isPlayerTurn = False
        aiMove()


def buttonPress7():
    global isPlayerTurn
    if btn7.cget("text") == " O " or btn7.cget("text") == " X ":

        writeLabel.config(text="Don't select an already selected box")
    else:
        btn7.config(background= 'blue', text= " X ")
        isPlayerTurn = False
        aiMove()


def buttonPress8():
    global isPlayerTurn
    if btn8.cget("text") == " O " or btn8.cget("text") == " X ":

        writeLabel.config(text="Don't select an already selected box")
    else:
        btn8.config(background= 'blue', text= " X ")
        isPlayerTurn = False
        aiMove()


def buttonPress9():
    global isPlayerTurn
    if btn9.cget("text") == " O " or btn9.cget("text") == " X ":

        writeLabel.config(text="Don't select an already selected box")
    else:
        btn9.config(background= 'blue', text= " X ")
        isPlayerTurn = False
        aiMove()

def gameEndCheck():
    global isPlayerTurn
    if (btn1.cget("text")== " X " and btn2.cget("text")== " X " and btn3.cget("text"))== " X " or (btn4.cget("text")== " X " and btn5.cget("text")== " X " and btn6.cget("text"))== " X " or (btn7.cget("text")== " X " and btn8.cget("text")== " X " and btn9.cget("text")) == " X " or (btn1.cget("text")== " X " and btn5.cget("text")== " X " and btn9.cget("text"))== " X " or (btn3.cget("text")== " X " and btn5.cget("text")== " X " and btn7.cget("text"))==" X " or (btn1.cget("text")==" X " and btn4.cget("text")==" X " and btn7("text"))==" X " or (btn2.cget("text")==" X " and btn5.cget("text")==" X " and btn8.cget("text"))==" X " or (btn3.cget("text")==" X " and btn6.cget("text")==" X " and btn9.cget("text"))==" X ":
        writeLabel.config(text= 'You won!')
        isPlayerTurn= True
        mainwindow.after(3000, exit)
    
    elif (btn1.cget("text")== " O " and btn2.cget("text")== " O " and btn3.cget("text"))== " O " or (btn4.cget("text")== " O " and btn5.cget("text")== " O " and btn6.cget("text"))== " O " or (btn7.cget("text")== " O " and btn8.cget("text")== " O " and btn9.cget("text")) == " O " or(btn1.cget("text")== " O " and btn5.cget("text")== " O " and btn9.cget("text"))== " O " or (btn3.cget("text")== " O " and btn5.cget("text")== " O " and btn7.cget("text"))==" O " or (btn1.cget("text")==" O " and btn4.cget("text")==" O " and btn7.cget("text"))==" O " or (btn2.cget("text")==" O " and btn5.cget("text")==" O " and btn8.cget("text"))==" O " or (btn3.cget("text")==" O " and btn6.cget("text")==" O " and btn9.cget("text"))==" O ":
        writeLabel.config(text= 'You lost!')
        isPlayerTurn= True
        mainwindow.after(3000, exit)
    elif all(btn.cget("text") != "     " for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]):
        writeLabel.config(text='We drew!')
        isPlayerTurn = True
        mainwindow.after(3000, exit)

#look for the next comment if you want to skip this mess of ai's turn
def aiMove():
    global isPlayerTurn
    gameEndCheck()
    buttonguesser= random.randint(1,9)
    if isPlayerTurn == False:
        if buttonguesser == 1:
            if btn1.cget("text") != " O " and btn1.cget("text") != " X ":
                btn1.config(background= 'red', text= " O ")
                isPlayerTurn = True
                gameEndCheck()
                    
            else:
                aiMove()
        elif buttonguesser == 2:
            if btn2.cget("text") != " O " and btn2.cget("text") != " X ":
                btn2.config(background= 'red', text= " O ")
                isPlayerTurn = True
                gameEndCheck()
                    
            else:
                aiMove()
        elif buttonguesser == 3:
            if btn3.cget("text") != " O " and btn3.cget("text") != " X ":
                btn3.config(background= 'red', text= " O ")
                isPlayerTurn = True
                gameEndCheck()
                    
            else:
                aiMove()
        elif buttonguesser == 4:
            if btn4.cget("text") != " O " and btn4.cget("text") != " X ":
                btn4.config(background= 'red', text= " O ")
                isPlayerTurn = True
                gameEndCheck()
                    
            else:
                aiMove()
        elif buttonguesser == 5:
            if btn5.cget("text") != " O " and btn5.cget("text") != " X ":
                btn5.config(background= 'red', text= " O ")
                isPlayerTurn = True
                gameEndCheck()
                    
            else:
                aiMove()
        elif buttonguesser == 6:
            if btn6.cget("text") != " O " and btn6.cget("text") != " X ":
                btn6.config(background= 'red', text= " O ")
                isPlayerTurn = True
                gameEndCheck()
                    
            else:
                aiMove()
        elif buttonguesser == 7:
            if btn7.cget("text") != " O " and btn7.cget("text") != " X ":
                btn7.config(background= 'red', text= " O ")
                isPlayerTurn = True
                gameEndCheck()
                    
            else:
                aiMove()
        elif buttonguesser == 8:
            if btn8.cget("text") != " O " and btn8.cget("text") != " X ":
                btn8.config(background= 'red', text= " O ")
                isPlayerTurn = True
                gameEndCheck()
                    
            else:
                aiMove()
        elif buttonguesser == 9:
            if btn9.cget("text") != " O " and btn9.cget("text") != " X ":
                btn9.config(background= 'red', text= " O ")
                isPlayerTurn = True
                gameEndCheck()
                    
            else:
                aiMove()
    else:
        isPlayerTurn= True



#You managed to get through that mess, have a cookie!





nameLabel= tk.Label(text= "Noughts and Crosses \n")
            






btnMap = {
    1: ("btn1", buttonPress1),
    2: ("btn2", buttonPress2),
    3: ("btn3", buttonPress3),
    4: ("btn4", buttonPress4),
    5: ("btn5", buttonPress5),
    6: ("btn6", buttonPress6),
    7: ("btn7", buttonPress7),
    8: ("btn8", buttonPress8),
    9: ("btn9", buttonPress9),
}
for i in btnMap:
    globals()[btnMap[i][0]] = tk.Button(text="     ", command=btnMap[i][1])
btnList= [btn1.cget("text"), btn2.cget("text"), btn3.cget("text"), btn4.cget("text"), btn5.cget("text"), btn6.cget("text"), btn7.cget("text"), btn8.cget("text"), btn9.cget("text")]





nameLabel.grid(row=0, column=1)
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)

btn7.grid(row=5, column=0)
btn8.grid(row=5, column=1)
btn9.grid(row=5, column=2)
writeLabel.grid(row=9, column=1)
mainwindow.mainloop()
