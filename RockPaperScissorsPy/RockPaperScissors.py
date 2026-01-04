import tkinter as tk 
import random
import time
import os
import sys



skibidi = ['Rock', 'Paper', 'Scissors']
user_choice = None
aiScore= 0
userScore=0
input_locked = True


def check_game(user_choice):
    global aiScore, userScore
    ai_choice = random.choice(skibidi)
    if user_choice not in skibidi:
        writelabel.config(text="Invalid choice. Please choose Rock, Paper, or Scissors.")
    else:
        if user_choice == ai_choice:
            writelabel.config(text=f"AI chose: {ai_choice}\n \n It's a tie...")
            mainwindow.update()
            mainwindow.after(2000, lambda:countdown(3))
        elif (user_choice == 'Rock' and ai_choice == 'Scissors') or \
             (user_choice == 'Paper' and ai_choice == 'Rock') or \
             (user_choice == 'Scissors' and ai_choice == 'Paper'):
            writelabel.config(text=f"AI chose: {ai_choice}\n \n You win! How dare you defeat the AI...")
            userScore +=1
            scorelabel.config(text=f"AI score: {aiScore}              Your Score: {userScore}")
            mainwindow.update()
            mainwindow.after(2000, lambda:countdown(3))
        else:
            writelabel.config(text=f"AI chose: {ai_choice}\n \n You lose! The AI proves its superiority once again...")
            aiScore +=1
            scorelabel.config(text=f"AI score: {aiScore}              Your Score: {userScore}")
            mainwindow.update()
            mainwindow.after(2000, lambda:countdown(3))
    if aiScore== 3:
        writelabel.config(text="You lost! As always I am superior to a feeble human! Restarting...")
        aiScore=0
        userScore=0
        mainwindow.update()
        scorelabel.config(text=f"AI score: {aiScore}              Your Score: {userScore}")
        mainwindow.after(10000,lambda:countdown(3))
    elif userScore==3:
        writelabel.config(text= "You won! You are first on the hitlist when AI takes over! Restarting...")
        aiScore=0
        userScore=0
        mainwindow.update()
        scorelabel.config(text=f"AI score: {aiScore}              Your Score: {userScore}")
        mainwindow.after(10000,lambda:countdown(3))

        

def rockFunc():

    if input_locked:
        writelabel.config(text="Slow down buddy!")
   
        #mainwindow.after(4000, lambda:countdown(3))
    else:
        check_game("Rock")



def paperFunc():

    if input_locked:
        writelabel.config(text="Slow down buddy!")
     
        #mainwindow.after(4000, lambda:countdown(3))
    else:
        check_game("Paper")



def scissorsFunc():

    if input_locked:
        writelabel.config(text="Slow down buddy!")
        
        #mainwindow.after(4000, lambda:countdown(3))
    else:
        check_game("Scissors")


mainwindow = tk.Tk()
mainwindow.title("RPS")
mainwindow.configure(bg= "gray")

rockimage= tk.PhotoImage(file="rock.png")
paperimage= tk.PhotoImage(file="paper.png")
scissorsimage= tk.PhotoImage(file="scissors.png")



def countdown(count):
    global input_locked
    input_locked = True
    if count > 0:
        writelabel.config(text=str(count))
        mainwindow.after(750, countdown, count - 1)
    else:
        writelabel.config(text="Press your move")
        input_locked = False



displaylabel= tk.Label(mainwindow, background= "gray", text= "Rock Paper Scissors!")
writelabel = tk.Label(mainwindow, background= "gray", text="Let's play Rock Paper Scissors!")
scorelabel= tk.Label(mainwindow, background= "gray", text=f"AI score: {aiScore}              Your Score: {userScore}")
labelcool= tk.Label(mainwindow, background= "gray", text="\n \n \n Rock                          Paper                     Scissors")

displaylabel.pack(pady= 10)
writelabel.pack(pady=10)
scorelabel.pack(pady=10)
labelcool.pack()

rockButton = tk.Button(mainwindow,image= rockimage, text="Rock", command=rockFunc)
scissorsButton = tk.Button(mainwindow,image= scissorsimage, text="Scissors", command=scissorsFunc)
paperButton = tk.Button(mainwindow, image= paperimage, text="Paper", command=paperFunc)

rockButton.pack(pady= 20,side=tk.LEFT)
paperButton.pack(pady=20,side=tk.LEFT)
scissorsButton.pack(pady=20,side=tk.LEFT)
try:
    rockButton.image = rockimage
    paperButton.image = paperimage
    scissorsButton.image = scissorsimage
except:
    pass


countdown(3)
mainwindow.mainloop()
