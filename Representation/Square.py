from Generation import Conway_Reader
import Draw
import itertools

conway = Conway_Reader.conway_array

pixels = []

for N in range(1,12):

 input = [conway[N]]
 output = list(map(int, str(input[0])))
 input.append(output)
 pixels.append(output)


merged = list(itertools.chain(*pixels))
n = 10
final = [merged[i * n:(i + 1) * n] for i in range((len(merged) + n - 1) // n)]
pixels = final


Draw.Draw(pixels,0,10,1000,1000,0,0)