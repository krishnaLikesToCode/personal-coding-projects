
FOCUSCLR = '\033[93m'#yellow
RESET='\033[0;94m'
print("Use WASD to navigate!\n\n")
def displayBoard(board,focusedIndex):
    focusedIndex-=1
    print("\t._____._____._____.")
    for i in range(0,len(board),3):
        print("\t|     |     |     |")
        print(f"\t|  {FOCUSCLR if i==focusedIndex else RESET}{board[i]+RESET}  |  {FOCUSCLR if i+1==focusedIndex else RESET}{board[i+1]+RESET}  |  {FOCUSCLR if i+2==focusedIndex else RESET}{board[i+2]+RESET}  |")

        print("\t|_____|_____|_____|")

def checkIfValidIndex(index):return index>=0 and index<=9
board="*********"
cIndex=5;
count=0;
displayBoard(board,cIndex)
while True:
    mark="X" if count%2==0 else "O"
    hi=str(input("\nUse WASD to move, enter to add mark:\t"))
    if 'w' in hi and checkIfValidIndex(cIndex-3):cIndex-=3;
    
    elif 's' in hi and checkIfValidIndex(cIndex+3):cIndex+=3;

    elif 'a' in hi and checkIfValidIndex(cIndex-1) and cIndex not in [1,4,7]:cIndex-=1;
    
    elif 'd' in hi and checkIfValidIndex(cIndex+1) and cIndex not in [3,6,9]:cIndex+=1;

    elif hi==''and board[cIndex-1]=='*':board=list(board);board[cIndex-1]=mark;board="".join(board);count+=1;

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    displayBoard(board,cIndex)





