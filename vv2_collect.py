from vv2 import *

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
            which = ai_move(state, symbol, round)
        print(f'jin-cerdas memilih untuk mengisi baris {which[0]} dan kolom {which[1]}')
        
    print(player)
    latest_move[symbol == o] = (which[0]-1, which[1]-1)
    state[which[0]-1][which[1]-1] = symbol
    
def play(opponent):
    global f
    board = [[e,e,e,e,e] for i in range(5)]
    
    round = 1
    for i in range(5):
        for j in range(5):
            if board[i][j] == x or board[i][j] == o:
                round += 1

    moveFirst = opponent
    moveAfter = opponent

    
        
        
    while terminal(board) == False:
        symbol = [o,x][round % 2]
        whoseTurn = [moveAfter, moveFirst][round%2]
        move(board, whoseTurn, symbol, round)
        round += 1
        if round >= 7:
            f.write(str(round) + ';' + stringState(board))
            f.write('\n')
    
    print(f" -------------------------------------------- -----SELESAI----- --------------------------------------------")
    printBoard(board)
    print(f" -------------------------------------------- -----SELESAI----- --------------------------------------------")

def ai_move(state, symbol, round):
    bestScore = [-10,10][symbol == o]
    isMaximize = [True, False][symbol == o]
    count = 0
    
    for row in range(1,6):
        for col in range(1,6):
            if state[row-1][col-1] == e :
                if round < 5:
                    if ((row-1,col-1) in nearby(latest_move[symbol == o])):
                        start = time.time()
                        state[row-1][col-1] = symbol
                        score = minimax(state, not(isMaximize), depth = 6)
                        # print(f'Jin cerdas: jika saya memilih baris ke-{row} dan kolom ke-{col} maka menurut saya posisi akan terevaluasi {score}')
                        f3.write(stringState(state)+';'+str(score)+'\n')
                        
                        state[row-1][col-1] = e
                    else:
                        start = time.time()
                        state[row-1][col-1] = symbol
                        score = minimax(state, not(isMaximize), depth = 4)
                        # print(f'Jin cerdas: jika saya memilih baris ke-{row} dan kolom ke-{col} maka menurut saya posisi akan terevaluasi {score}')
                        f3.write(stringState(state)+';'+str(score)+'\n')
                        
                        state[row-1][col-1] = e
                else:
                    state[row-1][col-1] = symbol
                    if round <= 11:
                        score = minimax(state, not(isMaximize), depth = 6)
                    elif round <= 16:
                        score = minimax(state, not(isMaximize), depth = 6)
                    elif round <= 18:
                        score = minimax(state, not(isMaximize), depth = 8)
                    elif round <= 22:
                        score = minimax(state, not(isMaximize), depth = 6)
                    else:
                        score = minimax(state, not(isMaximize), depth = 6)
                    # print(f'Jin cerdas: jika saya memilih baris ke-{row} dan kolom ke-{col} maka menurut saya posisi akan terevaluasi {score}')
                    f3.write(stringState(state)+';'+str(score)+'\n')
                    state[row-1][col-1] = e
                
                end = time.time()
                print(end-start, "seconds")
                if isMaximize:

                    if score > bestScore:
                        bestScore = score
                        bestMove = (row, col)
                    
                        
                        
                else:
                    if  score < bestScore:
                        bestScore = score
                        bestMove = (row, col)
                    
                    
                        
    f2.write(stringState(state)+';'+str(bestMove)+'\n')           
    return bestMove

f = open('vv2_played.csv', 'a')
f2 = open('vv2_database.csv', 'a')
f3 = open('vv2_minimax_helper.csv', 'a')
for i in range(50):
    play('jin-cerdas')
f.close()
f2.close()
f3.close()