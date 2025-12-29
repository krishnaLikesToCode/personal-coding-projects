import random
print("Welcome to chess but made by a person who doesn't know what he's doing!")
hi=str(input("\nWould you like to play singleplayer or multiplayer (type s or m)?\t")).strip().lower()
if hi=='m':aiOn=False
else:
    aiOn=True
    hi2=int(input("AI difficulty: easy (0), medium (1), hard- needs good PC (2), extreme- needs NASA computer (3).\nType your answer\t"))
    if hi2==0:depth=0
    elif hi2==1:depth=1
    elif hi2==2:depth=3
    else:depth=5
LETTERS=['A','B','C','D','E','F','G','H']
NUMBERS=['1','2','3','4','5','6','7','8']
BLACK = '\033[93m'#yellow
WHITE = '\033[0;94m'#blue
ALPHA='abcdefgh'
RESET='\033[0m'
board = [
    # Black back rank
    [['b',' ♜  ','Rook'], ['b',' ♞  ','Knight'], ['b',' ♝  ','Bishop'], ['b',' ♛  ','Queen'], ['b',' ♚  ','King'], ['b',' ♝  ','Bishop'], ['b',' ♞  ','Knight'], ['b',' ♜  ','Rook']],
    # Black pawns
    [['b',' ♟  ','Pawn'], ['b',' ♟  ','Pawn'], ['b',' ♟  ','Pawn'], ['b',' ♟  ','Pawn'], ['b',' ♟  ','Pawn'], ['b',' ♟  ','Pawn'], ['b',' ♟  ','Pawn'], ['b',' ♟  ','Pawn']],
    # Empty row
    [['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None]],
    # Empty row
    [['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None]],
    # Empty row
    [['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None]],
    # Empty row
    [['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['    ','    ', None], ['   ','    ', None], ['    ','    ', None]],
    # White pawns
    [['w',' ♙  ','Pawn'], ['w',' ♙  ','Pawn'], ['w',' ♙  ','Pawn'], ['w',' ♙  ','Pawn'], ['w',' ♙  ','Pawn'], ['w',' ♙  ','Pawn'], ['w',' ♙  ','Pawn'], ['w',' ♙  ','Pawn']],
    # White back rank
    [['w',' ♖  ','Rook'], ['w',' ♘  ','Knight'], ['w',' ♗  ','Bishop'], ['w',' ♕  ','Queen'], ['w',' ♔  ','King'], ['w',' ♗  ','Bishop'], ['w',' ♘  ','Knight'], ['w',' ♖  ','Rook']],
]
#board functions/subprograms
def printBoard():#prints the current board
    global board 
    print(f'\n {RESET+"—".join(['' for i in range(56)])}\n'.join([f"{WHITE+(str(8-row))}{(RESET+'|').join([f' {WHITE+piece[1]} ' if piece[0]=='b' else f' {BLACK+piece[1]} ' for piece in board[row]])}" for row in range(8)]))
    print("\n    A      B      C      D      E      F      G      H\n\n")

def getState(cell,board):#returns cell values in form [color,icon,piece/state] and takes cell code as arg
    return board[7-(int(cell[1])-1)][ALPHA.index(cell[0].lower())]

def getListPos(cell):#returns list pos of a cell in form [row,column] and takes cell code as arg
    return ([(7-(int(cell[1])-1)),(ALPHA.index(cell[0].lower()))])

def movePiece(newCell,oldCell,b=None):#subroutine to move a piece to a new cell,takes new cell code and old cell code as args
    global board
    if b is None:
        tboard=board
    else:tboard=b
    nCellPos=getListPos(newCell)
    oldCellPos=getListPos(oldCell)
    thing=getState(oldCell,tboard)
    tboard[nCellPos[0]][nCellPos[1]]=thing
    if (thing[2]=='Pawn' and ((thing[0]=='w' and newCell[1]=='8') or (thing[0]=='b' and newCell[1]=='1'))):
        pawnPromotion(newCell,tboard)
    tboard[oldCellPos[0]][oldCellPos[1]]=['    ','    ',None]

    return tboard


def getUpRow(curCell,amm):#gets row that is a specified amount above, takes current/relative cell and distance as args
    if((int(curCell[1])+amm))<=8:return int(curCell[1])+amm
    return '?'
def getDownRow(curCell,amm):#gets row that is a specified amount below, takes current/relative cell and distance as args
    if((int(curCell[1])-amm))>=1:return int(curCell[1])-amm
    return '?'
def getLeftCol(curCell,amm):#gets column that is a specified amount to the left, takes current/relative cell and distance as args
    if (ALPHA.index(curCell[0].lower())-amm) >=0:
        return ALPHA[ALPHA.index(curCell[0].lower())-amm]
    return '?'
def getRightCol(curCell,amm):#gets column that is a specified amount to the right, takes current/relative cell and distance as args
    if (ALPHA.index(curCell[0].lower())+amm) <=7:
        return ALPHA[ALPHA.index(curCell[0].lower())+amm]
    return '?'
def pawnPromotion(cell,b):cellPos=getListPos(cell);b[cellPos[0]][cellPos[1]]=[f'{getState(cell,b)[0]}',' ♛  ','Queen']
def checkPieceAmm(piece,color):#finds ammount of pieces of a specified color, takes piece to find and color as args
    global board
    piecesFound=0
    for i in board:
        for j in i:
            if j[2]==piece and j[0]==color:piecesFound+=1
    return piecesFound
def copyBoard(board):return [[cell[:] for cell in row] for row in board]

def undoMove(board, old, new, captured,capturing):
    oldPos = getListPos(old)
    newPos = getListPos(new)
    board[oldPos[0]][oldPos[1]] = capturing
    board[newPos[0]][newPos[1]] = captured

def checkIfCheckOnPlayer(board,s_clr):
    pcsToCheck=[]
    kingPos=None
    queenPos=[]
    allvMoves=[]
    kingChecks=0
    queenChecks=0
    for i in LETTERS:
        for j in NUMBERS:
            m=getState(i+j,board)
            if m[0]!=s_clr and m[0].strip()!='':
                pcsToCheck.append(i+j)
            if m[0]==s_clr and m[2]=='King':
                kingPos=i+j
            if m[0]==s_clr and m[2]=='Queen':
                queenPos.append(i+j)
    for i in pcsToCheck:
        pieceM=PieceMoves(getState(i,board)[2],'None',i,False,True,board)
        vMoves=pieceM.chooseMoveSetAndRun()
        for j in vMoves:
            allvMoves.append(j)
    if kingPos in allvMoves and kingPos!=None:
        kingChecks+=1
    if len(queenPos)!=0:
        for i in queenPos:
            if i in allvMoves:
                queenChecks+=1
                break
    return [queenChecks,kingChecks]
class PieceMoves:#class that contains all pieces individual movesets
    def __init__(self,piece,cellToMoveTo,curCell,showValidMoves,isAI,board=None):#initialising function for class
        self.piece=piece
        self.cellToMoveTo=cellToMoveTo
        self.curCell=curCell
        self.showValidMoves=showValidMoves
        self.isAI=isAI
        self.board=board
    def pawnMoves(self):#pawn moveset 
        validMoves=[]
        basicMoves=[] 
        takingMoves=[]

        if getState(self.curCell,self.board)[0]=='w':
            basicMoves.append(f'{self.curCell[0]}{getUpRow(self.curCell,1)}')
            takingMoves.append(f'{getLeftCol(self.curCell,1)}{getUpRow(self.curCell,1)}')
            takingMoves.append(f'{getRightCol(self.curCell,1)}{getUpRow(self.curCell,1)}')
            if int(self.curCell[1])==2:basicMoves.append(f'{self.curCell[0]}{getUpRow(self.curCell,2)}')
        else:
            basicMoves.append(f'{self.curCell[0]}{getDownRow(self.curCell,1)}')
            takingMoves.append(f'{getLeftCol(self.curCell,1)}{getDownRow(self.curCell,1)}')
            takingMoves.append(f'{getRightCol(self.curCell,1)}{getDownRow(self.curCell,1)}')
            if int(self.curCell[1])==7:basicMoves.append(f'{self.curCell[0]}{getDownRow(self.curCell,2)}')
        for i in basicMoves:
            try:
                if getState(i,self.board)[2] is None and '?' not in i:  validMoves.append(i.upper())
            except:pass
        for i in takingMoves:
            try:
                if getState(i,self.board)[2] is not None and getState(i,self.board)[0] != getState(self.curCell,self.board)[0] and '?' not in i:   validMoves.append(i.upper())
            except:pass
        if self.isAI:return validMoves
        if len(validMoves)==0:return -2#no possible moves
        if self.showValidMoves==True:
            print(f"Valid moves are:    {','.join(validMoves)}")
            return -1#repeat player turn
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell,self.board)
            #if (getState(self.cellToMoveTo,self.board)[0]=='b' and self.cellToMoveTo[1]=='1') or (getState(self.cellToMoveTo,self.board)[0]=='w' and self.cellToMoveTo[1]=='8'):pawnPromotion(self.cellToMoveTo)
        else:return 0#invalid error
        return 1#success

    def chooseMoveSetAndRun(self):#function that is called, finds piece type and runs respective moveset
        match self.piece:
            case 'Pawn':
                return self.pawnMoves()
            case 'King':
                return self.kingMoves()
            case 'Queen':
                return self.queenMoves()
            case 'Rook':
                return self.rookMoves()
            case 'Bishop':
               return self.bishopMoves()
            case 'Knight':
               return self.knightMoves()
            case _:
                return -3# -3 is none in cell error
    def kingMoves(self):#king moveset
        moves=[]
        validMoves=[]
        try:moves.append(f'{self.curCell[0]}{getUpRow(self.curCell,1)}')
        except:pass
        try:moves.append(f'{self.curCell[0]}{getDownRow(self.curCell,1)}')
        except:pass
        try:moves.append(f'{getLeftCol(self.curCell,1)}{self.curCell[1]}')
        except:pass
        try:moves.append(f'{getRightCol(self.curCell,1)}{self.curCell[1]}')
        except:pass
        try:moves.append(f'{getLeftCol(self.curCell,1)}{getUpRow(self.curCell,1)}')
        except:pass
        try:moves.append(f'{getLeftCol(self.curCell,1)}{getDownRow(self.curCell,1)}')
        except:pass
        try:moves.append(f'{getRightCol(self.curCell,1)}{getUpRow(self.curCell,1)}')
        except:pass
        try:moves.append(f'{getRightCol(self.curCell,1)}{getDownRow(self.curCell,1)}')
        except:pass
        for i in moves:
            if '?' not in i:
                if getState(i,self.board)[2] is None or getState(i,self.board)[0]!= getState(self.curCell,self.board)[0] :validMoves.append(i.upper())

        if self.isAI:return validMoves
        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'Valid moves are:    {",".join(validMoves)}')
            return -1
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell,self.board)
        else:return 0
        return 1
    def queenMoves(self):#queen moveset
        moves=[]
        validMoves=[]
        for amm in range(1,8):
            moves.append(f'{self.curCell[0]}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{self.curCell[0]}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{self.curCell[1]}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{self.curCell[1]}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break

        for i in moves:
            if '?' not in i:
                if getState(i,self.board)[2] is None or getState(i,self.board)[0]!= getState(self.curCell,self.board)[0] :validMoves.append(i.upper())
        if self.isAI:return validMoves
        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'Valid moves are:    {",".join(validMoves)}')
            return -1
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell,self.board)
        else:return 0
        return 1
    def bishopMoves(self):#bishop moveset
        
        moves=[]
        validMoves=[]
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break

        for i in moves:
            if '?' not in i:
                if getState(i,self.board)[2] is None or getState(i,self.board)[0]!= getState(self.curCell,self.board)[0] :validMoves.append(i.upper())
        if self.isAI:return validMoves
        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'Valid moves are:    {",".join(validMoves)}')
            return -1
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell,self.board)
        else:return 0
        return 1

    def rookMoves(self):#rook moveset
        moves=[]
        validMoves=[]
        for amm in range(1,8):
            moves.append(f'{self.curCell[0]}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{self.curCell[0]}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{self.curCell[1]}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{self.curCell[1]}')
            if '?' in moves[-1]:break
            if getState(moves[-1],self.board)[2] is not None:break
        for i in moves:
            if '?' not in i:
                if getState(i,self.board)[2] is None or getState(i,self.board)[0]!= getState(self.curCell,self.board)[0] :validMoves.append(i.upper())
        if self.isAI:return validMoves
        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'Valid moves are:    {",".join(validMoves)}')
            return -1
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell,self.board)
        else:return 0
        return 1

    def knightMoves(self):#knight moveset
        moves=[]
        validMoves=[]
        moves.append(f'{getLeftCol(self.curCell,1)}{getUpRow(self.curCell,2)}')
        moves.append(f'{getLeftCol(self.curCell,1)}{getDownRow(self.curCell,2)}')
        moves.append(f'{getRightCol(self.curCell,1)}{getUpRow(self.curCell,2)}')
        moves.append(f'{getRightCol(self.curCell,1)}{getDownRow(self.curCell,2)}')
        moves.append(f'{getRightCol(self.curCell,2)}{getUpRow(self.curCell,1)}')
        moves.append(f'{getRightCol(self.curCell,2)}{getDownRow(self.curCell,1)}')
        moves.append(f'{getLeftCol(self.curCell,2)}{getUpRow(self.curCell,1)}')
        moves.append(f'{getLeftCol(self.curCell,2)}{getDownRow(self.curCell,1)}')

        for i in moves:
            if '?' not in i:
                if getState(i,self.board)[0]!=getState(self.curCell,self.board)[0] or getState(i,self.board)[2] is None:
                    validMoves.append(i.upper())
        if self.isAI:return validMoves

        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'\n\nValid moves are:    {",".join(validMoves)}')
            return -1

        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell,self.board)
        else:return 0
        return 1


#engine code
def lookUpVal(piece):
    match piece:
        case 'Pawn':
            return 1
        case 'Rook':
            return 5
        case 'Bishop':
            return 4
        case 'Knight':
            return 3
        case 'Queen':
            return 9
        case 'King':
            return 1000
        case _:
            return 0

def boardValCalc(board,player):
    tVal=0
    for n,i in enumerate(board):
        for x,j in enumerate(i):
            val=lookUpVal(j[2])
            clr= j[0]
            if clr==player:tVal+=val
            else:tVal-=val
    qAndKchecksOnSelf=checkIfCheckOnPlayer(board,player)
    if qAndKchecksOnSelf[0]!=0:tVal-=(3.1)
    if qAndKchecksOnSelf[1]!=0:tVal-=(1000)
    qAndKchecksOnOpp=checkIfCheckOnPlayer(board,'w' if player!='w' else 'b')
    if qAndKchecksOnOpp[0]!=0:tVal+=(3.1)
    if qAndKchecksOnOpp[1]!=0:tVal+=(1000)
    return tVal

def simulate(board,player,d,cPlayerBest=-100,oPlayerBest=100): 
    piecesToCheck=[]
    bestMove=None
    for i in LETTERS:
        for j in NUMBERS:
            cCell=i+j
            if getState(cCell,board)[0]==player:piecesToCheck.append(cCell)
    random.shuffle(piecesToCheck)
    for i in piecesToCheck:
        capturingMoves=[]
        quietMoves=[]
        stf=getState(i,board)
        thing=PieceMoves(stf[2],'None',i,False,True,board)
        moves=thing.chooseMoveSetAndRun()
        sortedMoves=[]
        if len(moves)==0:pass
        else:
            for j in moves:
                if getState(j,board)[2] is not None:capturingMoves.append(j)
                else:quietMoves.append(j)
            capturingMoves.sort(key=lambda m: lookUpVal(getState(m,board)[2]), reverse=True)
            sortedMoves=capturingMoves+quietMoves
            for j in sortedMoves:
                affectedPiece=getState(j,board)[:]
                capturingPiece=getState(i,board)[:]
                movePiece(j,i,board)
                if checkIfCheckOnPlayer(board,player)[1]:#checks if move leads to king getting checked (and prunes)
                    undoMove(board,i,j,affectedPiece,capturingPiece)
                    continue
                otherPlayer='b' if player=='w' else 'w'
                if d>0:
                    futureMove=simulate(board,otherPlayer,d-1, -oPlayerBest,-cPlayerBest)
                    score=-futureMove[2] if futureMove else boardValCalc(board,player)
                    
                else:
                    score=boardValCalc(board,player)
                    
                moveAndScore=[i,j,score]
                undoMove(board,i,j,affectedPiece,capturingPiece)
                if score > cPlayerBest or bestMove==None:bestMove=moveAndScore
                cPlayerBest=max(cPlayerBest,score)

                if cPlayerBest >= oPlayerBest:
                     return bestMove
    return bestMove





#player loop
count=0
while True:
    player='white'
    if count % 2 !=0:player='black'
    if aiOn and player=='black':
        aiMoveChoice=simulate(board,'b',depth)
        movePiece(aiMoveChoice[1],aiMoveChoice[0],board)
        p=getState(aiMoveChoice[1],board)
        print(f"Black moved the {p[2].lower()} in {aiMoveChoice[0]} to {aiMoveChoice[1]}")
        count+=1
        continue

    print(f"{(BLACK+player.capitalize()) if player=='white' else(WHITE+player.capitalize())}'s turn to play\n")
    listVals=False
    while True:#move validation loop
        printBoard() 
        if player=='white':prompt=str(input("Enter move in form '<old> to <new>' or type 'list <square>' ")).strip().upper()
        else:prompt=str(input(f"{WHITE}Enter move in form '<old> to <new>' or type 'list <square>' ")).strip().upper()

        if 'LIST' in prompt:
            listVals=True;x=prompt.replace('LIST','').strip();y='None'
            try:piece=getState(x,board);break
            except:print("\nInvalid cell");continue
        prompt=prompt.lower().replace(' ','').split('to')
        if len(prompt)!=2:print("\nInvalid format, enter in form (a2->a3)\n");continue
        x,y=prompt[0],prompt[1]
        piece=getState(x,board)
        if piece[0]!=player[0]:print(f"\nYou can't move {x}, it's not your piece!\n");continue
        break
    userInput=PieceMoves(piece[2],y,x,listVals,False,board)#assigns users inputs as a class object
    status=userInput.chooseMoveSetAndRun()#runs respective moveset from PieceMoves class
    match status:#checks status of previous moves
        case -3:print("Square empty")
        case -2:print("No possible moves")
        case -1:continue
        case 0:print("Invalid move")
        case 1:print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");count+=1
    if checkPieceAmm('King','b')==0:print('White wins');exit()
    elif checkPieceAmm('King','w')==0:print('Black wins');exit()

 
