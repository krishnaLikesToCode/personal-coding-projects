import random
while True:
    import time
    guessamount= 0
    print("Welcome to the number game")
    userguesswanted= int(input("How many chances do you want to guess my number?"))
    print("You want" ,userguesswanted, "guesses?")
    userconfirm= input()
    if userconfirm== "yes":
        print("")
    else:
        print("Restarting...")
        continue
    randnum= random.randint(1,100)
    time.sleep(1)
    score = 0
    while True:
        if guessamount== userguesswanted:
            usercontinuelose= str(input("You lost! To play again, type 'again', to end type 'end'"))
            usercontinuelose.lower
            if usercontinuelose == 'again':
                print('Restarting...')
                break
            else: 
                exit()
        guessamount += 1

        userguess= int(input("Guess my number!"))
        try:

            userguess
        except ValueError:
            print("Are you stewpid mate? Answer the question")
        if userguess > randnum:
            score += 1
            print("My number is lower")
    
        elif userguess == randnum:
            print('You won!, you took' , score, 'guesses.')
            usercontinue=str(input("To play again, type 'again', to end type 'end'"))
            usercontinue.lower()
            if usercontinue == 'again':
                print('Restarting...')
                break
            else: 
                exit()

        elif userguess < randnum:
            score +=1
            print("My number is higher")
    continue
        

