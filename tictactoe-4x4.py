import LCG
import time
e = ' '
x = 'X'
o = 'O'

def minimax_with_depth(state, is_maximizing, depth=1):
    # Define symbols for the game
    EMPTY = 'e'
    PLAYER_O = 'o'
    PLAYER_X = 'x'

    # Check if the game state is terminal and return its utility
    if terminal(state):
        return [utility(state), depth]

    # Set the current player's symbol based on whether it's maximizing or minimizing
    current_symbol = PLAYER_X if is_maximizing else PLAYER_O

    # Initialize the best score and corresponding depth based on the player
    best_score = -10 if is_maximizing else 10
    best_score_depth = None

    # Iterate over the game board to explore possible moves
    for row in range(3):
        for col in range(3):
            if state[row][col] == EMPTY:
                # Make the move
                state[row][col] = current_symbol

                # Recursively call minimax_with_depth with the updated state and depth
                score_depth = minimax_with_depth(state, not is_maximizing, depth + 1)

                # Undo the move
                state[row][col] = EMPTY

                # Update the best score and depth based on the new result
                if is_maximizing:
                    if score_depth[0] > best_score:
                        best_score = score_depth[0]
                        best_score_depth = score_depth
                    elif score_depth[0] == best_score and score_depth[1] < best_score_depth[1]:
                        best_score_depth = score_depth
                else:
                    if score_depth[0] < best_score:
                        best_score = score_depth[0]
                        best_score_depth = score_depth
                    elif score_depth[0] == best_score and score_depth[1] < best_score_depth[1]:
                        best_score_depth = score_depth

    return best_score_depth

def print_board(board):
    print("                             >>>>>            =================")
    for row in board:
        print("                             >>>>>            ||", end=' ')
        for cell in row:
            print(cell, end=' || ')
        print()
    print("                             >>>>>            =================")


def user_move(state):
    while True:
        row = int(input("Enter row: (1/2/3) "))
        col = int(input("Enter col: (1/2/3) "))

        if 1 <= row <= 3 and 1 <= col <= 3:
            if state[row - 1][col - 1] == 'e':
                return row, col
            else:
                print("Maaf, tetapi tuan harus memilih tempat yang belum diisi.")
        else:
            print("Tuan, masukan baris dan kolom harus berupa bilangan bulat dari 1 sampai 3.")


def bocil_move(state):
    empty_cells = list_of_empty_cells(state)
    while True:
        random_value = LCG.randint(0, 9)
        if empty_cells[random_value] != (-1, -1):
            return empty_cells[random_value]


def jin_cerdas_move(state, symbol, round_number):
    if round_number == 1:
        return 2, 2
    else:
        move_with_best_score = ai_move(state, symbol)
        random_value = LCG.randint(0, count_possible_moves(move_with_best_score) - 1)
        return move_with_best_score[random_value]


def move(state, player, symbol, round_number):
    print(f" -------------------------------------------- -----RONDE {round_number}----- --------------------------------------------")
    print_board(state)
    print(f" -------------------------------------------- -----RONDE {round_number}----- --------------------------------------------")

    if player == 'user':
        print('Giliranmu, Tuan, pilih baris dan kolom yang ingin dipilih.')
        chosen_move = user_move(state)
    elif player == 'bocil':
        print('*Bocil berpikir keras*')
        time.sleep(1.5)
        chosen_move = bocil_move(state)
        print(f'bocil memilih untuk mengisi baris {chosen_move[0]} dan kolom {chosen_move[1]}')
    elif player == 'jin-cerdas':
        print('jin-cerdas sedang berpikir...')
        time.sleep(1)
        print('Masih berpikir...')
        time.sleep(1)
        chosen_move = jin_cerdas_move(state, symbol, round_number)
        print(f'jin-cerdas memilih untuk mengisi baris {chosen_move[0]} dan kolom {chosen_move[1]}')

    state[chosen_move[0] - 1][chosen_move[1] - 1] = symbol

def count_possible_moves(possible_moves):
    i = 0
    move = possible_moves[i]
    while move != (-1, -1, -1):
        i += 1
        move = possible_moves[i]
    return i


def list_of_empty_cells(state):
    empty_cells = [(-1, -1) for _ in range(10)]
    count = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] == e:
                empty_cells[count] = (i + 1, j + 1)
                count += 1
    return empty_cells

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
                return 1
            elif (state[i][0] == state[i][1] and state[i][1] == state[i][2] and state[i][3] == state[i][2] and state[i][0] == o) or (state[0][i]==state[1][i] and state[1][i]==state[2][i] and state[2][i]==state[3][i] and state[0][i] == o):
                return -1

        # OR, IF THERE IS DIAGONAL LINE
        if ((state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[2][2] == state[3][3]) or (state[3][0] == state[1][2] and state[2][1] == state[1][2] and state[1][2] == state[0][3])) and (state[0][3] == x or state[0][0] == x):
            return 1
        elif ((state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[2][2] == state[3][3]) or (state[3][0] == state[1][2] and state[2][1] == state[1][2] and state[1][2] == state[0][3])) and (state[0][3] == o or state[0][0] == o):
            return -1
        
        else: # IF IT IS NOT BOTH OF THEM, THEN IT'S A DRAW!
            return 0

def ai_move(state, symbol):
    # Inisialisasi variabel
    best_score = [-10, 10][symbol == 'o']
    is_maximizing = [True, False][symbol == 'o']
    best_move = [(-1, -1, -1) for _ in range(10)]
    count = 0
    best_depth = None

    # Iterasi melalui papan permainan untuk mencari gerakan terbaik
    for row in range(3):
        for col in range(3):
            if state[row][col] == 'e':
                # Lakukan gerakan
                state[row][col] = symbol

                # Hitung skor dan kedalaman menggunakan fungsi minimax_with_depth
                score_depth = minimax_with_depth(state, not(is_maximizing))

                # Kembalikan keadaan sebelumnya
                state[row][col] = 'e'

                # Perbarui gerakan terbaik berdasarkan skor dan kedalaman baru
                if is_maximizing:
                    if score_depth[0] == best_score:
                        if score_depth[1] == best_depth:
                            best_move[count] = (row, col, score_depth[1])
                            count += 1
                        elif score_depth[1] < best_depth:
                            count = 0
                            best_move = [(-1, -1, -1) for _ in range(10)]
                            best_move[count] = (row, col, score_depth[1])
                            count += 1
                            best_depth = score_depth[1]
                    elif score_depth[0] > best_score:
                        best_score = score_depth[0]
                        count = 0
                        best_move = [(-1, -1, -1) for _ in range(10)]
                        best_move[count] = (row, col, score_depth[1])
                        count += 1
                        best_depth = score_depth[1]
                else:
                    if score_depth[0] == best_score:
                        if score_depth[1] == best_depth:
                            best_move[count] = (row, col, score_depth[1])
                            count += 1
                        elif score_depth[1] < best_depth:
                            count = 0
                            best_move = [(-1, -1, -1) for _ in range(10)]
                            best_move[count] = (row, col, score_depth[1])
                            count += 1
                            best_depth = score_depth[1]
                    elif score_depth[0] < best_score:
                        best_score = score_depth[0]
                        count = 0
                        best_move = [(-1, -1, -1) for _ in range(10)]
                        best_move[count] = (row, col, score_depth[1])
                        count += 1
                        best_depth = score_depth[1]

    return best_move



def play(opponent):
    print('Selamat datang di permainan tictactoe!')
    user_choice = int(input('Silakan pilih apakah anda ingin menjadi player pertama atau player kedua? (1/2) '))
    while user_choice != 1 and user_choice != 2:
        print('Pilihlah 1 atau 2, jangan ngadi-ngadi pilih angka lain.')
        user_choice = int(input('Silakan pilih apakah anda ingin menjadi player pertama atau player kedua? (1/2) '))

    board = [[e, e, e] for _ in range(4)]

    round_number = 1
    if user_choice == 1:
        user_symbol = x
        move_first = 'user'
        move_after = opponent
    else:
        user_symbol = o
        move_first = opponent
        move_after = 'user'

    while not terminal(board):
        symbol = x if round_number % 2 else o
        whose_turn = move_first if round_number % 2 else move_after
        move(board, whose_turn, symbol, round_number)
        round_number += 1

    print(" -------------------------------------------- -----SELESAI----- --------------------------------------------")
    print_board(board)
    print(" -------------------------------------------- -----SELESAI----- --------------------------------------------")

    game_result = utility(board)

if __name__ == '__main__':
    play(opponent='jin-cerdas')