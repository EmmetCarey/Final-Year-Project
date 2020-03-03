from Generation import Conway_Reader
import time
import Draw
import itertools

conway = Conway_Reader.conway_array
average = []
box_size = 3
length =  20

def getT(n):

    add = []
    count2 = 0

    t = n
    t1 = [conway[t]]
    t2 = [conway[t+3]]
    t1 = list(map(int, str(t1[0])))
    t2 = list(map(int, str(t2[0])))

    count = 0

    for i in range(0,len(t1)):
        if t1[i] == t2[i]:
           count += 1
           add.append(1)
        else:
            if t1[i] != t2[i]:
                break

    for i in range(count,len(t2)):
        t2[i] = 4

    g = float(len(add))/float(len(conway[t+3]))
    average.append(g)

    x = 70
    t2 = [t2[i * x:(i + 1) * x] for i in range((len(t2) + x - 1) // x)]

    return t2


width = box_size * len(conway[length-2])
merged = list(itertools.chain(*conway))
n = 10000000000
final = [merged[i * n:(i + 1) * n] for i in range((len(merged) + n - 1) // n)]

length = len(final[i])

for i in range(1,32):
    start_time = time.clock()
    array = getT(i)
    Draw.Draw(array,1,box_size,length,width,-200,300)

print average
d = 0
for i in range(5,len(average)):
    d+=average[i]

print d/len(average)