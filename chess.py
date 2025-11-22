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

def getState(cell):#returns cell values in form [color,icon,piece/state] and takes cell code as arg
    global board
    cellInBoard= board[7-(int(cell[1])-1)][ALPHA.index(cell[0].lower())]
    return cellInBoard

def getListPos(cell):#returns list pos of a cell in form [row,column] and takes cell code as arg
    global board
    return (x:=[(7-(int(cell[1])-1)),(ALPHA.index(cell[0].lower()))])

def movePiece(newCell,oldCell):#subroutine to move a piece to a new cell,takes new cell code and old cell code as args
    global board
    nCellPos=getListPos(newCell)
    oldCellPos=getListPos(oldCell)
    print(board[nCellPos[0]][nCellPos[1]])
    print(getState(oldCell))
    board[nCellPos[0]][nCellPos[1]]=getState(oldCell)
    board[oldCellPos[0]][oldCellPos[1]]=['    ','    ',None]
    print(board[nCellPos[0]][nCellPos[1]])
    print(getState(oldCell))

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
def checkPieceAmm(piece,color):#finds ammount of pieces of a specified color, takes piece to find and color as args
    global board
    piecesFound=0
    for i in board:
        for j in i:
            if j[2]==piece and j[0]==color:piecesFound+=1
    return piecesFound

class PieceMoves:#class that contains all pieces individual movesets
    def __init__(self,piece,cellToMoveTo,curCell,showValidMoves):#initialising function for class
        self.piece=piece
        self.cellToMoveTo=cellToMoveTo
        self.curCell=curCell
        self.showValidMoves=showValidMoves
    def pawnMoves(self):#pawn moveset 
        validMoves=[]
        basicMoves=[] 
        takingMoves=[]

        if getState(self.curCell)[0]=='w':
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
                if getState(i)[2] is None and '?' not in i:  validMoves.append(i.upper())
            except:pass
        for i in takingMoves:
            try:
                if getState(i)[2] is not None and getState(i)[0] != getState(self.curCell)[0] and '?' not in i:   validMoves.append(i.upper())
            except:pass
        if len(validMoves)==0:return -2#no possible moves
        if self.showValidMoves==True:
            print(f"Valid moves are:    {','.join(validMoves)}")
            return -1#repeat player turn
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell)
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
        global board
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
                if getState(i)[2] is None or getState(i)[0]!= getState(self.curCell)[0] :validMoves.append(i.upper())
        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'Valid moves are:    {",".join(validMoves)}')
            return -1
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell)
        else:return 0
        return 1
    def queenMoves(self):#queen moveset
        moves=[]
        validMoves=[]
        for amm in range(1,8):
            moves.append(f'{self.curCell[0]}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{self.curCell[0]}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{self.curCell[1]}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{self.curCell[1]}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break

        for i in moves:
            if '?' not in i:
                if getState(i)[2] is None or getState(i)[0]!= getState(self.curCell)[0] :validMoves.append(i.upper())
        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'Valid moves are:    {",".join(validMoves)}')
            return -1
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell)
        else:return 0
        return 1
    def bishopMoves(self):#bishop moveset
        moves=[]
        validMoves=[]
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break

        for i in moves:
            if '?' not in i:
                if getState(i)[2] is None or getState(i)[0]!= getState(self.curCell)[0] :validMoves.append(i.upper())
        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'Valid moves are:    {",".join(validMoves)}')
            return -1
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell)
        else:return 0
        return 1

    def rookMoves(self):#rook moveset
        moves=[]
        validMoves=[]
        for amm in range(1,8):
            moves.append(f'{self.curCell[0]}{getUpRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{self.curCell[0]}{getDownRow(self.curCell,amm)}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getLeftCol(self.curCell,amm)}{self.curCell[1]}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for amm in range(1,8):
            moves.append(f'{getRightCol(self.curCell,amm)}{self.curCell[1]}')
            if '?' in moves[-1]:break
            if getState(moves[-1])[2] is not None:break
        for i in moves:
            if '?' not in i:
                if getState(i)[2] is None or getState(i)[0]!= getState(self.curCell)[0] :validMoves.append(i.upper())
        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'Valid moves are:    {",".join(validMoves)}')
            return -1
        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell)
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
                if getState(i)[0]!=getState(self.curCell)[0] or getState(i)[2] is None:
                    validMoves.append(i.upper())

        if len(validMoves)==0:return -2
        if self.showValidMoves==True:
            print(f'\n\nValid moves are:    {",".join(validMoves)}')
            return -1

        if self.cellToMoveTo.upper() in validMoves:
            movePiece(self.cellToMoveTo,self.curCell)
        else:return 0
        return 1

count=0
while True:#player loop
    player='white'
    if count % 2 !=0:player='black'
    print(f"{(BLACK+player.capitalize()) if player=='white' else(WHITE+player.capitalize())}'s turn to play\n")
    listVals=False
    while True:#move validation loop
        printBoard() 
        if player=='white':prompt=str(input("Enter move in form '<old> to <new>' or type 'list <square>' ")).strip().upper()
        else:prompt=str(input(f"{WHITE}Enter move in form '<old> to <new>' or type 'list <square>' ")).strip().upper()

        if 'LIST' in prompt:
            listVals=True;x=prompt.replace('LIST','').strip();y='None'
            try:piece=getState(x);break
            except:print("\nInvalid cell");continue
        prompt=prompt.lower().replace(' ','').split('to')
        if len(prompt)!=2:print("\nInvalid format, enter in form (a2->a3)\n");continue
        x,y=prompt[0],prompt[1]
        piece=getState(x)
        if piece[0]!=player[0]:print(f"\nYou can't move {x}, it's not your piece!\n");continue
        break
    userInput=PieceMoves(piece[2],y,x,listVals)#assigns users inputs as a class object
    status=userInput.chooseMoveSetAndRun()#runs respective moveset from PieceMoves class
    match status:#checks status of previous moves
        case -3:print("Square empty")
        case -2:print("No possible moves")
        case -1:continue
        case 0:print("Invalid move")
        case 1:print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");count+=1
    if checkPieceAmm('King','b')==0:print('White wins');exit()
    elif checkPieceAmm('King','w')==0:print('Black wins');exit()

               
