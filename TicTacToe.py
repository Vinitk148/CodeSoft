board ={1:" ", 2:" ", 3:" ",
        4:" ", 5:" ", 6:" ",
        7:" ", 8:" ", 9:" ",}

def Show():
    print()
    print(board[1], " | ",board[2], " | ",board[3])
    print("---|-----|---")
    print(board[4], " | ",board[5], " | ",board[6])
    print("---|-----|---")
    print(board[7], " | ",board[8], " | ",board[9])
    print()
    
def CheckDraw():
    for i in board.values():
        if i == " ":
            return False
    return True

def CheckWinner(player):
    #for rows
    if board[1]==board[2] and board[1]==board[3] and board[1]==player:
        return True
    elif board[4]==board[5] and board[4]==board[6] and board[4]==player:
        return True
    elif board[7]==board[8] and board[7]==board[9] and board[7]==player:
        return True
    
    #for columns
    elif board[1]==board[4] and board[1]==board[7] and board[1]==player:
        return True
    elif board[2]==board[5] and board[2]==board[8] and board[2]==player:
        return True
    elif board[3]==board[6] and board[3]==board[9] and board[3]==player:
        return True
            
    #for cross
    elif board[1]==board[5] and board[1]==board[9] and board[1]==player:
        return True
    elif board[3]==board[5] and board[3]==board[7] and board[3]==player:
        return True
        
    else:
        return False

def insertpos(player , pos):
    if board[pos] == " ":
        board[pos] = player
        Show()
        if CheckWinner(player):
            print( "player" , player , "is win the game1")
            quit()

        if CheckDraw():
            print("Game Tie")
            quit()

    else:
        print("Position is already filled")
        pos = int(input("enter a new position = "))
        insertpos(player , pos)

Show()

p1="X"
p2="O"

while True:
    print (p1 , "chance")
    pos=int(input("enter position (1-9) = "))
    insertpos(p1, pos)
    print (p2 , " chance")
    pos=int(input("enter position (1-9) = "))
    insertpos(p2, pos)