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
    for y in range(4):
        print("                             >>>>>            =====================")
        print("                             >>>>>            ||", end = ' ')
        for x in range(4):
            print(board[y][x], end ='')
            print(" ||", end = ' ')
        print()
    print("                             >>>>>            =====================")
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
            if (1<= row and row <= 4) and (1 <= col and col <=4):
                if state[which[0] -1][which[1]-1] != e:
                    print("Maaf, tetapi tuan harus memilih tempat yang belum diisi..")
                else:
                    break
            else:
                print("Tuan, masukan baris dan kolom harus berupa bilangan bulat dari 1 sampai 3.")
        
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
            which = (1,1)
        else:
            movesWithBestScore = ai_move(state, symbol)
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
    result = [(-1,-1) for i in range(10)]
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == e:
                result[count] = (i+1,j+1)
                count += 1
    
    return result

def ai_move(state, symbol):
    bestScore = [-10,10][symbol == o]
    isMaximize = [True, False][symbol == o]
    bestMove = [(-1,-1) for i in range(30)]
    count = 0
    
    for row in range(1,5):
        for col in range(1,5):
            if state[row-1][col-1] == e:
                state[row-1][col-1] = symbol
                score = minimax(state, not(isMaximize), depth = 5)
                print(f'Jin-cerdas: "Jika saya memilih baris {row} dan kolom {col}, posisinya akan terevaluasi {score}.')
                state[row-1][col-1] = e
                
                if isMaximize:

                    if score > bestScore:
                        bestScore = score
                        count = 0
                        bestMove[count] = (row, col)
                        count += 1
                    
                    elif score == bestScore:
                        bestMove[count] = (row, col)
                        count += 1
                        
                        
                else:
                    if  score < bestScore:
                        bestScore = score
                        count = 0
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
        return utility(state)
    
    symbol = [o,x][isMaximizing]
    bestScore = [10,-10][isMaximizing]
    for row in range(1,5):
        for col in range(1,5):
            if state[row-1][col-1] == e:
                state[row-1][col-1] = symbol
                score = minimax(state, not(isMaximizing), depth - 1)
                state[row-1][col-1] = e
                
                if isMaximizing:
                    if score > bestScore:
                        bestScore = score
                    
                    if bestScore >= 1:
                        return bestScore
                            
                else:
                    if score < bestScore:
                        bestScore = score
                    
                    if bestScore <= -1:
                        return bestScore
                        
                    
    
    
    return bestScore
    
    

def minimax_withdepth(state, isMaximizing, depth = 1):
    if terminal(state):
        return [utility(state), depth]
    
    symbol = [o,x][isMaximizing]
    bestScore = [10,-10][isMaximizing]
    for row in range(1,5):
        for col in range(1,5):
            if state[row-1][col-1] == e:
                state[row-1][col-1] = symbol
                Score_Depth = minimax_withdepth(state, not(isMaximizing), depth + 1)
                state[row-1][col-1] = e
                
                updated = False
                if isMaximizing:
                    if Score_Depth[0] > bestScore:
                        bestScore_Depth = Score_Depth
                        updated = True
                    elif Score_Depth[0] == bestScore:
                        if Score_Depth[1] < bestScore_Depth[1]:
                            bestScore_Depth = Score_Depth
                            updated = True
                            
                else:
                    if Score_Depth[0] < bestScore:
                        bestScore_Depth = Score_Depth
                        updated = True
                    elif Score_Depth[0] == Score_Depth:
                        if Score_Depth[1] < bestScore_Depth[1]:
                            bestScore_Depth = Score_Depth
                            updated = True
                            
                bestScore = bestScore_Depth[0]
                    
    
    
    return bestScore_Depth
    
        
        
    
    
    
def terminal(state):
    
    check = True
    
    #no more empty cell returns True
    for i in range(4):
        for j in range(4):
            if state[i][j] == e:
                check = False
    
    #but, if there is straight (('X' or 'O') and not 'e') returns True 
    for i in range(4):
        if (state[i][0] == state[i][1] and state[i][1] == state[i][2] and state[i][3] == state[i][2] and state[i][0] != e) or (state[0][i]==state[1][i] and state[1][i]==state[2][i] and state[2][i]==state[3][i] and state[0][i] != e):
            check = True
    
    #or there is diagonal (('X' or 'O') and not 'e') returns True
    if ((state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[2][2] == state[3][3] and state[3][3] != e) or (state[3][0] == state[1][2] and state[2][1] == state[1][2] and state[1][2] == state[0][3] and state[0][3] != e)):
        check = True
    
    return check

def utility(state):
    if terminal(state) is False:
        return None
    else:
        
        # IF THERE IS STRAIGHT LINE
        for i in range(4):
            if (state[i][0] == state[i][1] and state[i][1] == state[i][2] and state[i][3] == state[i][2] and state[i][0] == x) or (state[0][i]==state[1][i] and state[1][i]==state[2][i] and state[2][i]==state[3][i] and state[0][i] == x):
                return 5
            elif (state[i][0] == state[i][1] and state[i][1] == state[i][2] and state[i][3] == state[i][2] and state[i][0] == o) or (state[0][i]==state[1][i] and state[1][i]==state[2][i] and state[2][i]==state[3][i] and state[0][i] == o):
                return -5

        # OR, IF THERE IS DIAGONAL LINE
        if ((state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[2][2] == state[3][3] and state[0][0] == x) or (state[3][0] == state[1][2] and state[2][1] == state[1][2] and state[1][2] == state[0][3] and state[0][3] == x)):
            return 5
        elif (state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[2][2] == state[3][3] and state[0][0] == o) or (state[3][0] == state[1][2] and state[2][1] == state[1][2] and state[1][2] == state[0][3] and state[0][3] == o):
            return -5
        
        else: # IF IT IS NOT BOTH OF THEM, THEN IT'S A DRAW!
            return evaluation(state)

def evaluation(state):
    
    eval = 0
    # 3 STRAIGHT:
    for i in range(4):
        for j in range(2):
            # HORIZONTAL
            if state[i][0+j] == state[i][1+j] and state[i][1+j] == state[i][2+j] and (state[i][0+j] in [x,o]):
                if state[i][0+j] == x:
                    eval += 1
                elif state[i][0+j] == o:
                    eval -= 1
            
            # vertikal
            elif state[0+j][i] == state[1+j][i] and state[1+j][i] == state[2+j][i] and (state[0+j][i] in [x,o]):
                if state[0+j][i] == x:
                    eval += 1
                elif state[0+j][i] == o:
                    eval -= 1
    
    # DIAGONAL
    for i in range(2):
        for j in range(2):
            
            if ((state[0+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[2+i][2+j])) and (state[0+i][0+j] in [x,o]):
                if state[0+i][0+j] == x:
                    eval += 1
                elif state[0+i][0+j] == o:
                    eval -= 1
            
            
            elif (state[2+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[0+i][2+j]) and (state[2+i][0+j] in [x,o]):
                if state[2+i][0+j] == x:
                    eval += 1
                elif state[2+i][0+j] == o:
                    eval -= 1
    
    return eval

def eval_x(state):
    eval = 0
    
    # 3 STRAIGHT:
    for i in range(4):
        for j in range(2):
            # HORIZONTAL
            if state[i][0+j] == state[i][1+j] and state[i][1+j] == state[i][2+j] and (state[i][0+j] in [x,o]):
                if state[i][0+j] == x:
                    eval += 1
            
            # vertikal
            elif state[0+j][i] == state[1+j][i] and state[1+j][i] == state[2+j][i] and (state[0+j][i] in [x,o]):
                if state[0+j][i] == x:
                    eval += 1
    
    for i in range(2):
        for j in range(2):
            if ((state[0+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[2+i][2+j])) and (state[0+i][0+j] in [x,o]):
                        if state[0+i][0+j] == x:
                            eval += 1
            elif (state[2+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[0+i][2+j]) and (state[2+i][0+j] in [x,o]):
                        if state[2+i][0+j] == x:
                            eval += 1
    return eval

def eval_o(state):
    eval = 0
    
    # 3 STRAIGHT:
    for i in range(4):
        for j in range(2):
            # HORIZONTAL
            if state[i][0+j] == state[i][1+j] and state[i][1+j] == state[i][2+j] and (state[i][0+j] in [x,o]):
                if state[i][0+j] == o:
                    print(f'1, i,j = {i,j}')
                    eval += 1
            
            # vertikal
            elif state[0+j][i] == state[1+j][i] and state[1+j][i] == state[2+j][i] and (state[0+j][i] in [x,o]):
                if state[0+j][i] == o:
                    print(f'2, i,j = {i,j}')
                    eval += 1
    
    for i in range(2):
        for j in range(2):
            if ((state[0+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[2+i][2+j])) and (state[0+i][0+j] in [x,o]):
                        if state[0+i][0+j] == o:
                            print(f'2, i,j = {i,j}')
                            eval += 1
            elif (state[2+i][0+j] == state[1+i][1+j] and state[1+i][1+j] == state[0+i][2+j]) and (state[2+i][0+j] in [x,o]):
                        if state[2+i][0+j] == o:
                            print(f'3, i,j = {i,j}')
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
        
    board = [[e,e,e,e] for i in range(4)]
    
    round = 1
    for i in range(4):
        for j in range(4):
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


    
        
        
            

        
        
if __name__ == '__main__':
    play(opponent='jin-cerdas')