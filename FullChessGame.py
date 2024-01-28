#FULL CHESS GAME
#Author: MomorioUHT
#Since 21 Jan 2024

import random
gameOver = False

chessBoard = [["R","N","B","K","Q","B","N","R"],
              ["P","P","P","P","P","P","P","P"],
              [" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "],
              ["p","p","p","p","p","p","p","p"],
              ["r","n","b","q","k","b","n","r"]]

def isAbleToMove(CurrState: str, Piece: str, oldX: int, oldY: int, newX: int, newY: int):
    print(" ")
    
def MovePiece(CurrState: str, Piece: str, oldX: int, oldY: int, newX: int, newY: int):
    avalibleMoves = []
    if Piece.lower() == "q":
        for i in range(0,8):
            if (oldY+i < 8 and oldX+i < 8): 
                if (chessBoard[oldY+i][oldX+i] != " "): avalibleMoves.append([oldY+i, oldX+i])
                break
        for i in range(0,8):
            if (oldY-i >= 0 and oldX-i >= 0): 
                if (chessBoard[oldY-i][oldX-i] != " "): avalibleMoves.append([oldY-i, oldX-i])
                break
        for i in range(0,8):
            if (oldY+i < 8 and oldX-i >= 0):
                if (chessBoard[oldY+i][oldX-i] == " "): avalibleMoves.append([oldY+i, oldX-i])
                break 
        for i in range(0,8):
            if (oldY-i >= 0 and oldX+i < 8): 
                if (chessBoard[oldY-i][oldX+i] == " "): avalibleMoves.append([oldY-i, oldX+i])
                break 
        for i in range(0,8):
            if (oldY-i >= 0):
                if (chessBoard[oldY-i][oldX] == " "): avalibleMoves.append([oldY-i, oldX])
                break 
        for i in range(0,8):
            if (oldY+i < 8): 
                if (chessBoard[oldY+i][oldX] == " "): avalibleMoves.append([oldY+i, oldX])
                break 
        for i in range(0,8):
            if (oldX-i >= 0): 
                if (chessBoard[oldY+i][oldX] == " "): avalibleMoves.append([oldY, oldX-i])
                break 
        for i in range(0,8):
            if (oldX+i < 8): 
                if (chessBoard[oldY][oldX+i] == " "): avalibleMoves.append([oldY, oldX+i])
                break  
    elif Piece.lower() == "b":
        for i in range(0,8):
            if (oldY+i < 8 and oldX+i < 8): 
                if (chessBoard[oldY+i][oldX+i] == " "): avalibleMoves.append([oldY+i, oldX+i])
                break  
            if (oldY-i >= 0 and oldX-i >= 0): 
                if (chessBoard[oldY-i][oldX-i] == " "): avalibleMoves.append([oldY-i, oldX-i])
                break  
            if (oldY+i < 8 and oldX-i >= 0): 
                if (chessBoard[oldY+i][oldX-i] == " "): avalibleMoves.append([oldY+i, oldX-i])
                break  
            if (oldY-i >= 0 and oldX+i < 8): 
                if (chessBoard[oldY-i][oldX+i] == " "): avalibleMoves.append([oldY-i, oldX+i]) 
                break 
    elif Piece.lower() == "r":
        for i in range(0,8):
            if (oldY-i >= 0): 
                if (chessBoard[oldY-i][oldX] == " "): avalibleMoves.append([oldY-i, oldX])
                break
            if (oldY+i < 8): 
                if (chessBoard[oldY+i][oldX] == " "):avalibleMoves.append([oldY+i, oldX])
                break
            if (oldX-i >= 0): 
                if (chessBoard[oldY][oldX-i] == " "): avalibleMoves.append([oldY, oldX-i])
                break
            if (oldX+i < 8): 
                if (chessBoard[oldY][oldX+i] == " "): avalibleMoves.append([oldY, oldX+i]) 
                break
    elif Piece.lower() == "k":
        if (oldY-1 >= 0): avalibleMoves.append([oldY-1, oldX])
        if (oldY+1 < 8): avalibleMoves.append([oldY+1, oldX])
        if (oldX-1 >= 0): avalibleMoves.append([oldY, oldX-1])
        if (oldX+1 < 8): avalibleMoves.append([oldY, oldX+1]) 
        if (oldY+1 < 8 and oldX+1 < 8): avalibleMoves.append([oldY+1, oldX+1])
        if (oldY-1 >= 0 and oldX-1 >= 0): avalibleMoves.append([oldY-1, oldX-1])
        if (oldY+1 < 8 and oldX-1 >= 0): avalibleMoves.append([oldY+1, oldX-1])
        if (oldY-1 >= 0 and oldX+1 < 8): avalibleMoves.append([oldY-1, oldX+1]) 
    elif Piece.lower() == "n":
        if (oldY+2 < 8 and oldX+1 < 8): avalibleMoves.append([oldY+2, oldX+1])
        if (oldY-2 >= 0 and oldX-1 >= 0): avalibleMoves.append([oldY-2, oldX-1])
        if (oldY+1 < 8 and oldX-2 >= 0): avalibleMoves.append([oldY+1, oldX-2])
        if (oldY-1 >= 0 and oldX+2 < 8): avalibleMoves.append([oldY-1, oldX+2])
        if (oldY+1 < 8 and oldX+2 < 8): avalibleMoves.append([oldY+1, oldX+2])
        if (oldY-1 >= 0 and oldX-2 >= 0): avalibleMoves.append([oldY-1, oldX-2])
        if (oldY+2 < 8 and oldX-1 >= 0): avalibleMoves.append([oldY+2, oldX-1])
        if (oldY-2 >= 0 and oldX+1 < 8): avalibleMoves.append([oldY-2, oldX+1])
    elif Piece.lower() == "p":
        if (CurrState == "Computer"): 
            if (oldY+1 != 8): avalibleMoves.append([oldY+1, oldX])
        elif (CurrState == "Player"): 
            if (oldY-1 != 0): avalibleMoves.append([oldY-1, oldX])
    
    if ([newY, newX] not in avalibleMoves):
        return False
    chessBoard[newY][newX] = Piece
    chessBoard[oldY][oldX] = " "
    avalibleMoves = []
    return True

def printChessBoard():
    print("  0 1 2 3 4 5 6 7 ")
    print("------------------")
    for i in range(8):
        print(f"{i}|", end="")
        for j in range(8):
            print(f"{chessBoard[i][j]}|", end="")
        print("\n------------------")
    
while(not gameOver):
    print("==================\n")
    printChessBoard()
    print("Your Turn")
    
    #PlayerMoves
    #Select Piece
    while(True):
        playerOldList = [int(i) for i in str(input("Select piece (Example 3 4): ")).split(" ")]
        if (chessBoard[playerOldList[1]][playerOldList[0]] == " "): 
            print("There is no any piece in that grid! Select new one.")
            continue
        elif (chessBoard[playerOldList[1]][playerOldList[0]].isupper()):
            print("That is not your piece!")
            continue    
        else:
            break
    #Let Player Move Valid Piece
    while(True):
        playerNewList = [int(i) for i in str(input("Next Move (Example 4 5): ")).split(" ")]        
        if (playerOldList[1] == playerNewList[1] and playerOldList[0] == playerNewList[0]):
            print("Next position cannot be the same as previous!")
            continue            
        elif (not MovePiece("Player", chessBoard[playerOldList[1]][playerOldList[0]], playerOldList[0], playerOldList[1], playerNewList[0], playerNewList[1])):
            print("Invalid Move!")
            continue 
        else:
            MovePiece("Player", chessBoard[playerOldList[1]][playerOldList[0]], playerOldList[0], playerOldList[1], playerNewList[0], playerNewList[1])
            break
        
    print("Computer is thinking....")
    #ComputerMoves
    #Select Piece
    while(True):
        computerOldList = [random.randint(0,7), random.randint(0,7)]
        if (chessBoard[computerOldList[1]][computerOldList[0]] == " "): 
            continue
        elif (chessBoard[computerOldList[1]][computerOldList[0]].islower()):
            continue    
        else:
            break
    #Move Valid Piece
    while(True):        
        computerNewList = [random.randint(0,7), random.randint(0,7)]
        if (computerOldList[1] == computerNewList[1] and computerOldList[0] == computerNewList[0]):
            continue            
        elif (not MovePiece("Computer", chessBoard[computerOldList[1]][computerOldList[0]], computerOldList[0], computerOldList[1], computerNewList[0], computerNewList[1])):
            continue 
        else:
            MovePiece("Computer", chessBoard[computerOldList[1]][computerOldList[0]], computerOldList[0], computerOldList[1], computerNewList[0], computerNewList[1])
            break