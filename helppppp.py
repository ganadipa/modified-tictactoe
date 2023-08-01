

# e = ' '
# x = 'X'
# o = 'O'

# def round(state):
#     return stringState(state).count(x) + stringState(state).count(o) + 1

# board = [[e for i in range(5) ] for i in range(5)]
# board[2][2]= x
# f = open('anjing.csv', 'w')


# numround = round(board)
# for i in range(24):
#     row = int(input('row: '))
#     col = int(input('col: '))
#     generatePossibleState(board)
#     board[row][col] = [o,x][numround%2]
#     numround += 1

# f.close()

import csv

f = open('anjing3.csv', 'w')
f1 = open('anjing.csv','r')
f2 = open('anjing2.csv', 'r')
states = csv.reader(f1)
state = []
eval = []
for i in states:
    state += i
for i in range(285):
    eval += [f2.readline().rstrip()]
    f2.readline()
print(state, eval)

for i in range(285):
    print(i)
    print(len(state), len(eval))
    f.write(state[i]+eval[i]+'\n')

f1.close()
f2.close()
f.close()