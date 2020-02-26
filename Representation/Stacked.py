from Generation import Conway_Reader
import Draw
import time
import itertools

conway = Conway_Reader.conway_array

pixels = []
length=  32
box_size = 10

for N in range(1,length):

 input = [conway[N]]
 output = list(map(int, str(input[0])))
 input.append(output)
 pixels.append(output)

width = box_size * len(pixels[length-2])
merged = list(itertools.chain(*pixels))
n = 10000000000
final = [merged[i * n:(i + 1) * n] for i in range((len(merged) + n - 1) // n)]
length = len(final[i])


start_time = time.time()
Draw.Draw(pixels,1,box_size,length,width,0,0)
print("--- %s seconds ---" % (time.time() - start_time))