from v4 import *

def play(opponent):
        
    board = [[e,e,e,e] for i in range(4)]
    
    round = 1
    for i in range(4):
        for j in range(4):
            if board[i][j] == x or board[i][j] == o:
                round += 1

    moveFirst = opponent
    moveAfter = opponent

        
        
    while terminal(board) == False:
        symbol = [o,x][round % 2]
        whoseTurn = [moveAfter, moveFirst][round%2]
        move(board, whoseTurn, symbol, round)
        round += 1
    
    print(f" -------------------------------------------- -----SELESAI----- --------------------------------------------")
    printBoard(board)
    print(f" -------------------------------------------- -----SELESAI----- --------------------------------------------")
play(opponent='jin-cerdas')