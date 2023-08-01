import time
import random
import os
os.path.dirname(__file__)
import LCG


x = "X"
o = "O"
e = " "


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

def ai_move(state, symbol, round):
    bestScore = [-10,10][symbol == o]
    isMaximize = [True, False][symbol == o]
    bestMove = [(-1,-1) for i in range(30)]
    count = 0
    
    for row in range(1,6):
        for col in range(1,6):
            if state[row-1][col-1] == e:
                state[row-1][col-1] = symbol
                if round <= 11:
                    score = minimax(state, not(isMaximize), depth = 3)
                elif round <= 16:
                    score = minimax(state, not(isMaximize), depth = 4)
                elif round <= 18:
                    score = minimax(state, not(isMaximize), depth = 6)
                elif round <= 22:
                    score = minimax(state, not(isMaximize), depth = 7)
                else:
                    score = minimax(state, not(isMaximize), depth = 3)
                print(f'Jin-cerdas: "Jika saya memilih baris {row} dan kolom {col}, posisinya akan terevaluasi {score}.')
                state[row-1][col-1] = e
                
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