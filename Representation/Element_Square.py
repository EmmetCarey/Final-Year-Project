from Generation import Conway_Reader
import Draw
import itertools

def getElements():

    f2 = open("/Users/emmetcarey/Documents/GitHub/Final-Year-Project/Text/Elements.txt", "r")

    elements = f2.read().split("\n")

    x = elements[3].split(" ")
    numbers = []
    for i in range(0,92):
        numbers.append(elements[i].split(" "))
    return numbers

def getT(element_number):

    test = []
    pixels = []

    for i in range(0,len(conway_array)):

        a = str(conway_array[i])
        b = str(numbers[element_number][1])
        d = a.replace(b,"4" * int(len(b)),a.find(b) + 1)
        test.append(d)

    for N in range(1,25):

     input = [test[N]]
     output = list(map(int, str(input[0])))
     input.append(output)
     pixels.append(output)

    merged = list(itertools.chain(*pixels))
    n = 30
    final = [merged[i * n:(i + 1) * n] for i in range((len(merged) + n - 1) // n)]
    return final

conway_array = Conway_Reader.conway_array
numbers = getElements()

for i in range(0, 20):
    array = getT(i)
    Draw.Draw(array,1,5,1000,1000)


