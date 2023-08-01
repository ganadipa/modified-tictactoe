import time
import random
import LCG
import multiprocessing
import concurrent.futures


x = "X"
o = "O"
e = " "

latest_move = [(2,2),(2,2)]


def nearby(move):
    lst = [(-1,-1) for i in range(9)]
    row = [(move[0] + i-1) for i in range(3)]
    col = [(move[1] + i-1) for i in range(3)]
    if move[0] == 0:  
        row.remove(-1)
    
    if move[0] == 5:
        row.remove(5)
    
    if move[1] == 0:
        col.remove(-1)
    
    if move[1] == 5:
        col.remove(5)
    
    count = 0
    for i in row:
        for j in col:
            if move == (i,j):
                continue
            lst[count] = (i,j)
            count += 1

    return lst
emptyGrid = [[e,e,e],
             [e,e,e],
             [e,e,e]]

def printBoard(board):
    for y in range(5):
        print("                             >>>>>            ===========================")
        print("                             >>>>>            ||", end = ' ')
        for x in range(5):
            print(board[y][x], end ='')
            print(" ||", end = ' ')
        print()
    print("                             >>>>>            ===========================")
    print(f'eval: {evaluation(board)}')
    print(f'eval X: {eval_x(board)}')
    print(f'eval O: {eval_o(board)}')

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
        time.sleep(1)
        print('Masih berpikir...')
        print()
        time.sleep(1)
        
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
    


def countPossibleMove(pos_move): #ONLY FOR AI
    i = 0
    move = pos_move[i]
    while move != (-1,-1):
        i += 1
        move = pos_move[i]
    return i
    
def listOfEmptyCell(state):
    result = [(-1,-1) for i in range(30)]
    count = 0
    for i in range(5):
        for j in range(5):
            if state[i][j] == e:
                result[count] = (i+1,j+1)
                count += 1
    
    return result

def possible_row_col(state):
    lst = []
    for i in range(5):
        for j in range(5):
            if state[i][j] == e:
                lst.append((i+1,j+1))
    return lst

def ai_move(state, symbol, round):
    bestScore = [-10,10][symbol == o]
    isMaximize = [True, False][symbol == o]
    bestMove = [(-1,-1) for i in range(30)]
    count = 0
    
    evaluated_row_col = []
    processes = []
    start = []
    return_dict = multiprocessing.Manager().dict()
    for row, col in possible_row_col(state):
        if (row,col) not in evaluated_row_col :
            start.append(time.time())
            if round < 5:
                if ((row-1,col-1) in nearby(latest_move[symbol == o])):
                    state[row-1][col-1] = symbol
                    p = multiprocessing.Process(target=minimax_WRD, args=[state, not(isMaximize), 3, return_dict])
                    p.start()
                    processes.append(p)
                    
                else:
                    continue
            else:
                state[row-1][col-1] = symbol
                if round <= 11:
                    p = multiprocessing.Process(target=minimax_WRD, args=[state, not(isMaximize), 4, return_dict])
                    p.start()
                    processes.append(p)
                elif round <= 16:
                    p = multiprocessing.Process(target=minimax_WRD, args=[state, not(isMaximize), 4, return_dict])
                    p.start()
                    processes.append(p)
                elif round <= 18:
                    p = multiprocessing.Process(target=minimax_WRD, args=[state, not(isMaximize), 6, return_dict])
                    p.start()
                    processes.append(p)
                elif round <= 22:
                    p = multiprocessing.Process(target=minimax_WRD, args=[state, not(isMaximize), 7, return_dict])
                    p.start()
                    processes.append(p)
                else:
                    p = multiprocessing.Process(target=minimax_WRD, args=[state, not(isMaximize), 3, return_dict])
                    p.start()
                    processes.append(p)
                
            state[row-1][col-1] = e
            evaluated_row_col.append((row,col))
            
    i = 0  
    for process in processes:
        process.join()
        print(time.time() - start[i], 'seconds')
        i += 1    
    for row, col in possible_row_col(state):
        if round < 5: 
            if ((row-1,col-1) in nearby(latest_move[symbol == o])):
                state[row-1][col-1] = symbol                  
            else:
                continue
        else:
            state[row-1][col-1] = symbol
            
        score = return_dict[str(state)]
        if isMaximize:

            if score > bestScore:
                bestScore = score
                count = 0
                bestMove = [(-1,-1) for i in range(30)]
                bestMove[count] = (row, col)
                count += 1
            
            elif score == bestScore:
                bestMove[count] = (row, col)
                count += 1
                
                
        else:
            if  score < bestScore:
                bestScore = score
                count = 0
                bestMove = [(-1,-1) for i in range(30)]
                bestMove[count] = (row, col)
                count += 1
            
            elif score == bestScore:
                bestMove[count] = (row, col)
                count += 1
        state[row-1][col-1] = e
                
                        
                
    print()
    
    return bestMove

def minimax(state, isMaximizing, depth):
    if depth == 0:
        return evaluation(state)
    if terminal(state):
        return evaluation(state)
    
    
    symbol = [o,x][isMaximizing]
    bestScore = [10,-10][isMaximizing]
    for row in range(1,6):
        for col in range(1,6):
            if state[row-1][col-1] == e:
                state[row-1][col-1] = symbol
                score = minimax(state, not(isMaximizing), depth - 1)
                state[row-1][col-1] = e
                
                if isMaximizing:
                    if score > bestScore:
                        bestScore = score
                    
                    # if bestScore >= 1:
                    #     return bestScore
                            
                else:
                    if score < bestScore:
                        bestScore = score
                    
                    # if bestScore <= -1:
                    #     return bestScore
                        
                    
    
    
    return bestScore
    
    


def minimax_WRD(state, isMaximizing, depth, return_dict):
    if depth == 0:
        return_dict[str(state)] = evaluation(state)
        return
    if terminal(state):
        return_dict[str(state)] = evaluation(state)
        return
    
    evaluated_row_col = []
    processes = []
        
    symbol = [o,x][isMaximizing]
    bestScore = [10,-10][isMaximizing]
    for row in range(1,6):
        for col in range(1,6):
            if state[row-1][col-1] == e:
                state[row-1][col-1] = symbol
                p = multiprocessing.Process(target=minimax_WRD, args=[state, not(isMaximizing), depth-1, return_dict])
                p.start()
                processes.append(p)
                evaluated_row_col.append((row,col))
                state[row-1][col-1] = e
    
    for process in processes:
        process.join()
    
    for row,col in evaluated_row_col:
        state[row-1][col-1] = symbol
        score = return_dict[str(state)]
    

        if isMaximizing:
            if score > bestScore:
                bestScore = score
            
            # if bestScore >= 1:
            #     return bestScore
                    
        else:
            if score < bestScore:
                bestScore = score
            
            # if bestScore <= -1:
            #     return bestScore
        state[row-1][col-1] = e
                        
                    
    
    return_dict[str(state)] = bestScore
    return
        
        
    
    
    
def terminal(state):
    
    check = True
    
    #no more empty cell returns True
    for i in range(5):
        for j in range(5):
            if state[i][j] == e:
                check = False
    

    return check


def evaluation(state):
    
    eval = 0
    # 3 STRAIGHT:
    for i in range(5):
        for j in range(3):
            # HORIZONTAL
            if state[i][0+j] == state[i][1+j] and state[i][1+j] == state[i][2+j] and (state[i][0+j] in [x,o]):
                if state[i][0+j] == x:
                    eval += 1
                if state[i][0+j] == o:
                    eval -= 1
            
            # vertikal
            if state[0+j][i] == state[1+j][i] and state[1+j][i] == state[2+j][i] and (state[0+j][i] in [x,o]):
                if state[0+j][i] == x:
                    eval += 1
                if state[0+j][i] == o:
                    eval -= 1
    
    # DIAGONAL
    for i in range(3):
        for j in range(3):
            
            if ((state[0+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[2+i][2+j])) and (state[0+i][0+j] in [x,o]):
                if state[0+i][0+j] == x:
                    eval += 1
                elif state[0+i][0+j] == o:
                    eval -= 1
            
            
            if (state[2+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[0+i][2+j]) and (state[2+i][0+j] in [x,o]):
                if state[2+i][0+j] == x:
                    eval += 1
                if state[2+i][0+j] == o:
                    eval -= 1
    
    return eval

def eval_x(state):
    eval = 0
    
    # 3 STRAIGHT:
    for i in range(5):
        for j in range(3):
            # HORIZONTAL
            if state[i][0+j] == state[i][1+j] and state[i][1+j] == state[i][2+j] and state[i][0+j] == x:
                print(f'hor straight x in {i}{j}')

                eval += 1
            
            # vertikal
            if state[0+j][i] == state[1+j][i] and state[1+j][i] == state[2+j][i] and state[0+j][i] == x:
                print(f'hor straight x in {i}{j}')
                eval += 1
    
    for i in range(3):
        for j in range(3):
            if ((state[0+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[2+i][2+j])) and state[0+i][0+j] == x:
                print(f'diag down-right x in {i}{j}')
                eval += 1
            if (state[2+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[0+i][2+j]) and  state[2+i][0+j] == x:
                print(f'diag right-top x in {i}{j}')
                eval += 1
                
    return eval

def eval_o(state):
    eval = 0
    
    # 3 STRAIGHT:
    for i in range(5):
        for j in range(3):
            # HORIZONTAL
            if state[i][0+j] == state[i][1+j] and state[i][1+j] == state[i][2+j] and state[i][0+j] == o:
                print(f'hor straight o in {i}{j}')

                eval += 1
            
            # vertikal
            if state[0+j][i] == state[1+j][i] and state[1+j][i] == state[2+j][i] and state[0+j][i] == o:
                print(f'hor straight o in {i}{j}')
                eval += 1
    
    for i in range(3):
        for j in range(3):
            if ((state[0+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[2+i][2+j])) and state[0+i][0+j] == o:
                print(f'diag down-right o in {i}{j}')
                eval += 1
            if (state[2+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[0+i][2+j]) and  state[2+i][0+j] == o:
                print(f'diag right-top o in {i}{j}')
                eval += 1
                
    return eval
    

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



    
        
        
            

        
        
if __name__ == '__main__':
    play(opponent='jin-cerdas')