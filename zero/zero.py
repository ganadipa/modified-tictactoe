from helper import stringState, minimax, realState, ai_move
import os
import csv
os.chdir(os.path.dirname(__file__))

e = ' '
x = 'X'
o = 'O'

def deepzero_helper(state):
    '''
    sta
    
    '''
    numround = stringState(state).count(x) + stringState(state).count(o) + 1
    file_round = 'data_'+str(numround)+'.csv'
    with open(file_round, 'r') as f:
        reader = csv.reader(f)
        

def update_data(numround):
    with open('data_3.csv', 'r') as f:
        reader = csv.reader(f,delimiter=';')
        count = 0
        for string_state, eval, bmove in reader:
            count += 1
            
            if bmove == '(-1,-1)':
                symbol = [x,o][numround%2]
                move, score = ai_move(realState(string_state), symbol, 4, depth = 3)
                f_write.write(string_state+';'+str(score)+';'+str(move)+'\n')
            
            if count % 20 == 0:
                print('done', count)

if __name__ == '__main__':
    f_write = open('data_3_write.csv', 'a')
    update_data(3)
    f_write.close()
    
    
                
                
        
    
    
    