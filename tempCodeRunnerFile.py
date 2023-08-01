        reader = csv.reader(file, delimiter=';')
        for state, score in reader: 
            tmp = realState(state)
            minimax_helper[state] = float(score)
            for x in possibleState(realState(state)):
                minimax_helper[stringState(x)] = float(score)