import os 
import csv
import copy
os.chdir(os.path.dirname(__file__))

e = ' '
x = 'X'
o = 'O'

def stringState(state):
    word = ''
    for i in state:
        for j in i:
            word += j
    return word

def round(state):
    return stringState(state).count('X') + stringState(state).count('O') + 1


def realState(stringState, size='5x5'):
    if size== '5x5':
        lst = [[e for i in range(5)]for i in range(5)]
        for i in range(25):
            lst[i//5][i%5] = stringState[i]
    return lst


def generatePossibleState(state):
    in_the_file = []
    for i in range(5):
        for j in range(5):
            if state[i][j] == e:
                symbol = [o,x][round(state)%2]
                state[i][j] = symbol
                
                for already_there_state in in_the_file:
                    if is_the_same(state, already_there_state):
                        break
                
                else:
                    f.write(stringState(state)+';'+'0'+';'+'(-1,-1)'+'\n')
                    tmp = [[state[i][j] for j in range(5)] for i in range(5)]
                    in_the_file.append(tmp)
                    
                
                state[i][j] = e
    

def is_the_same(state1, state2):
    if state2 in possibleState(state1):
        return True
    else:
        False
    ...

def rotate(state):
    tmp = [[state[i][j] for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[j][4-i] = state[i][j]
    
    return tmp

def mirroredState(state):
    res = []
    for row in state:
        res = [row] + res
    return res

def possibleState(state):
    real = copy.deepcopy(state)
    mirror = copy.deepcopy(mirroredState(state))
    
    res = []
    for i in range(4):
        res.append(rotate(real))
        res.append(rotate(mirror))
        real = copy.deepcopy(rotate(real))
        mirror = copy.deepcopy(rotate(mirror))
    
    return res


def generate(numround):
    global f
    if numround == 1:
        f = open('data_1.csv', 'w')
        generatePossibleState([[e for i in range(5)] for i in range(5)])
        f.close()
    
    
    if numround >= 2:
        prev_file = 'data_' + str(numround-1) + '.csv'
        curr_file = 'data_' + str(numround) + '.csv'
        f = open(curr_file, 'w')
        with open(prev_file, 'r') as prev_data:
            reader = csv.reader(prev_data, delimiter=';')
            for string_state, eval, bmove in reader:
                generatePossibleState(realState(string_state))
        f.close()

def printBoard(board):
    for y in range(5):
        print("                             >>>>>            ===========================")
        print("                             >>>>>            ||", end = ' ')
        for x in range(5):
            print(board[y][x], end ='')
            print(" ||", end = ' ')
        print()
    print("                             >>>>>            ===========================")
if __name__ == '__main__':
    for i in range(1,5):
        generate(i)    
    
    