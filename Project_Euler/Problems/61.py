triangle = [[a*(a+1)/2,a,'t'] for a in range(45,141)]   
square = [[a**2,a,'s'] for a in range(32,100)]
pentagonal = [[a*(3*a-1)/2,a,'p'] for a in range(26,82)]
hexagonal = [[a*(2*a-1),a,'hx'] for a in range(23,71)]
heptagonal = [[a*(5*a-3)/2,a,'hp'] for a in range(21,64)]
octagonal = [[a*(3*a-2),a,'o'] for a in range(19,59)]

big_list = [triangle,square,pentagonal,hexagonal,heptagonal,octagonal]

def seperate(a):
            return [[str(y[0])[0:2],str(y[0])[2:4],y[1],y[2]] for y in a if str(y[0])[2] != '0']

split_list = [seperate(a) for a in big_list]
                                    
def searcher(original,number,series,log=1, solution = False, counter = 0):
    if log == len(series):
        if number[1] == original[0]:
            solution = True
    else:
        while counter < len(series[log]) and not solution:
            if number[1] == series[log][counter][0]:
                solution = searcher(original, series[log][counter],series,log+1)
            counter += 1
    if solution == True:
        if log == len(series):
            print original, 0
        print number,log
    return solution


for x in split_list[0]:
    searcher(x,x,split_list)
    
import itertools    
bigger_list = [x for x in list(itertools.permutations(split_list))]

for a in bigger_list:
    for b in a[0]:
        searcher(b,b,a)
