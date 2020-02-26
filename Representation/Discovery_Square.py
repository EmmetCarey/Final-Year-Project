
import turtle
from Generation import Conway_Reader
import itertools
import Draw

conway_array = Conway_Reader.conway_array

def getTest(i):

    test = ""
    t = i
    t1 = [conway_array[t]]
    t2 = [conway_array[t+3]]
    t1 = list(map(int, str(t1[0])))
    t2 = list(map(int, str(t2[0])))

    for i in range(0,len(t1)):
        if t1[i] == t2[i]:
           test+=str((t1[i]))
        else:
            if t1[i] != t2[i]:
                break
    return test


for i in range(0,20):

    conway_replace = []


    for x in range(0,20):
        d = conway_array[x].replace(getTest(i), "4" * int(len(getTest(i))), conway_array[x].rfind(getTest(i)) + 1)
        conway_replace.append(list(map(int, str(d))))


    merged = list(itertools.chain(*conway_replace))
    n = 40
    final = [merged[i * n:(i + 1) * n] for i in range((len(merged) + n - 1) // n)]
    Draw.Draw(final,1,5)










