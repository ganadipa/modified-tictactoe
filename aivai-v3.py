from v3 import *

def play(opponent):
    print('Selamat datang di permainan tictactoe!')
    print('Silakan pilih apakah anda ingin menjadi player pertama atau player kedua? (1/2) ',end = '')
    ans = int(input())
    while ans != 1 and ans != 2:
        print('Pilihlah 1 atau 2, jangan ngadi-ngadi pilih angka lain.')
        print('Silakan pilih apakah anda ingin menjadi player pertama atau player kedua? (1/2) ',end = '')
        ans = int(input())
        
    board = [[e,e,e,e] for i in range(4)]
    
    round = 1
    for i in range(4):
        for j in range(4):
            if board[i][j] == x or board[i][j] == o:
                round += 1

    if ans == 1:
        userSymbol = x
        moveFirst = opponent
        moveAfter = opponent
    else:
        userSymbol = o
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
    if utility(board) == 1:
        if userSymbol == x:
            print(f'Selamat, Bandung telah memenangnkan permainan melawan {opponent}!')
        else:
            print(f'{opponent} telah memenangkan permainan!')
    elif utility(board) == -1:
        if userSymbol == o:
            print(f'Selamat, Bandung telah memenangnkan permainan melawan {opponent}!')
        else:
            print(f'{opponent} telah memenangkan permainan!')
    else:
        print(f'Permainan telah selesai! pertarungan tictactoe antara Bandung dengan {opponent} berakhir seri!')
play(opponent='jin-cerdas')