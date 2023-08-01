from v6 import *
def play(opponent):
    print('Selamat datang di permainan tictactoe!')
    print('Silakan pilih apakah anda ingin menjadi player pertama atau player kedua? (1/2) ',end = '')
    ans = int(input())
    while ans != 1 and ans != 2:
        print('Pilihlah 1 atau 2, jangan ngadi-ngadi pilih angka lain.')
        print('Silakan pilih apakah anda ingin menjadi player pertama atau player kedua? (1/2) ',end = '')
        ans = int(input())
        
    board = [[e,e,e,e,e] for i in range(5)]
    
    round = 1
    for i in range(5):
        for j in range(5):
            if board[i][j] == x or board[i][j] == o:
                round += 1

    if ans == 1:
        userSymbol = x
        moveFirst = 'user'
        moveAfter = opponent
    else:
        userSymbol = o
        moveFirst = opponent
        moveAfter = 'user'
        
        
    while terminal(board) == False:
        symbol = [o,x][round % 2]
        whoseTurn = [moveAfter, moveFirst][round%2]
        move(board, whoseTurn, symbol, round)
        round += 1
    
    print(f" -------------------------------------------- -----SELESAI----- --------------------------------------------")
    printBoard(board)
    print(f" -------------------------------------------- -----SELESAI----- --------------------------------------------")

play(opponent='jin-cerdas')