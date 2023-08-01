import time

randomValue = int(time.time())

def randint(start, end): #MENGENERATE RANDOM INTEGER PADA RANGE DARI START SAMPAI END SECARA INKLUSIF.
    global randomValue
    if end >= start:
        m = 2**32
        a = 1664525
        c = 1013904224
        
        randomValue = ((a*randomValue+c) % m) # new random value is for the next seed.
        r = randomValue/m # KARENA NILAI 0 <= x < m, maka 0 <= r < 1 dan start <= start + ((end-start)*r)//1 + 1 <= end
        result = start + int(((end-start+1)*r)//1)
        
        return result
    else:
        return 0

def randsample(n, start, end): #MENGENERATE LIST BERISI RANDOM INTEGER DENGAN PANJANG N PADA RANGE DARI START SAMPAI END SECARA INKLUSIF.
    lst = [0 for i in range(n)]
    for i in range(1, n+1):
        
        lst[i-1] = randint(start, end)
    return lst
