from Generation import Conway_Reader
import time
import Draw

conway = Conway_Reader.conway_array

def getT(n):

    t = n
    t1 = [conway[t]]
    t2 = [conway[t+3]]
    t1 = list(map(int, str(t1[0])))
    t2 = list(map(int, str(t2[0])))

    count = 0

    for i in range(0,len(t1)):
        if t1[i] == t2[i]:
           count += 1
        else:
            if t1[i] != t2[i]:
                break

    for i in range(count,len(t2)):
        t2[i] = 4

    x = 70
    t2 = [t2[i * x:(i + 1) * x] for i in range((len(t2) + x - 1) // x)]

    return t2

for i in range(1,25):
    start_time = time.clock()
    array = getT(i)
    Draw.Draw(array,1,5)
