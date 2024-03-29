from Generation import Conway_Reader
import Draw
import itertools

conway = Conway_Reader.conway_array

pixels = []

for N in range(1,25):

 input = [conway[N]]
 output = list(map(int, str(input[0])))
 input.append(output)
 pixels.append(output)


merged = list(itertools.chain(*pixels))
n = 40
final = [merged[i * n:(i + 1) * n] for i in range((len(merged) + n - 1) // n)]
pixels = final


Draw.Draw(pixels,0,5,1000,1000,0,300)