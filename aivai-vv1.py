from vv1 import *

def move(state, player, symbol, round):
    global latest_move
    print()
    print(f" -------------------------------------------- -----RONDE {round}----- --------------------------------------------")
    printBoard(state)
    print(f" -------------------------------------------- -----RONDE {round}----- --------------------------------------------")
    if player == 'user':
        print('Giliranmu, Tuan, pilih baris dan kolom yang ingin dipilih.')
        while True:
            row = int(input("Enter row: (1/2/3) "))
            col = int(input("Enter col: (1/2/3) "))
            print("\n")
            which = (row, col)
            if (1<= row and row <= 5) and (1 <= col and col <=5):
                if state[which[0] -1][which[1]-1] != e:
                    print("Maaf, tetapi tuan harus memilih tempat yang belum diisi..")
                else:
                    break
            else:
                print("Tuan, masukan baris dan kolom harus berupa bilangan bulat dari 1 sampai 5.")
        
        print(f'Bandung memiilih untuk mengisi baris {which[0]} dan kolom {which[1]}.')
        
    
    elif player == 'bocil':
        list_tempat_kosong = listOfEmptyCell(state)
        while True:
            randomValue = LCG.randint(0,9)
            if list_tempat_kosong[randomValue] != (-1,-1):
                break
        print('*Bocil berpikir keras*')
        print()
        time.sleep(1.5)
        which = list_tempat_kosong[randomValue]
        print(f'bocil memilih untuk mengisi baris {which[0]} dan kolom {which[1]}')
    
    elif player == 'jin-cerdas':
        
        print('jin-cerdas sedang berpikir...')
        print()
        print('Masih berpikir...')
        print()
        
        print(f'round: {round}')
        if round == 1:
            which = (3,3)
        else:
            movesWithBestScore = ai_move(state, symbol, round)
            print(movesWithBestScore)
            which= movesWithBestScore[LCG.randint(0,countPossibleMove(movesWithBestScore)-1)]
        print(f'jin-cerdas memilih untuk mengisi baris {which[0]} dan kolom {which[1]}')
        
    print(player)
    latest_move[symbol == o] = (which[0]-1, which[1]-1)
    state[which[0]-1][which[1]-1] = symbol
    
def play(opponent):
        
    board = [[e,e,e,e,e] for i in range(5)]
    
    round = 1
    for i in range(5):
        for j in range(5):
            if board[i][j] == x or board[i][j] == o:
                round += 1

    moveFirst = opponent
    moveAfter = opponent

    if round >= 7:
        f.write(str(round) + ';' + stringState(board))
        
        
    while terminal(board) == False:
        symbol = [o,x][round % 2]
        whoseTurn = [moveAfter, moveFirst][round%2]
        move(board, whoseTurn, symbol, round)
        round += 1
    
    print(f" -------------------------------------------- -----SELESAI----- --------------------------------------------")
    printBoard(board)
    print(f" -------------------------------------------- -----SELESAI----- --------------------------------------------")

f = open('vv1-played.csv', 'a')
for i in range(50):
    play(opponent='jin-cerdas')
f.close()