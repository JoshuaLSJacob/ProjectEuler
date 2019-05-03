hands_file = open('/Users/joshuajacob/Downloads/p054_poker.txt', 'r').read().split()
from operator import itemgetter

def num_func(num):
    if num == 'T':
        return(10)
    if num == 'J':
        return(11)
    if num == 'Q':
        return(12)
    if num == 'K':
        return(13)
    if num == 'A':
        return(14)
    if num == 'C':
        return(1)
    if num == 'D':
        return(2)
    if num == 'H':
        return(3)
    if num == 'S':
        return(4)
    else:
        return(int(num))


hands_file = [sorted([[num_func(x[0]),num_func(x[1])] for x in hands_file[5*i:5*i+5]]) for i in range(2000)]

print(hands_file[0])
print(sorted(hands_file[0], key = itemgetter(1)))

def frequency_checker(hand):
    z = [0 for m in range(14)]
    x = 0
    while x<5:
        z[hand[x][0]-1] += 1
        x += 1
    return(z)

def flush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1]:
        return(True)
    
def hand_checker(hand):
    freak = frequency_checker(hand)
    if max(freak) == 1:
        if hand[0][0]+4==hand[4][0]:
            if flush(hand):
                return('Straight Flush')
            else:
                return('Straight')

        elif flush(hand):
                return('Flush')
        else:
            return('High Card')
            
    elif max(freak) == 2:
        if freak.count(2) == 2:
            return('Two Pairs')
        else:
            return('Pair')
    elif max(freak) == 3:
        if freak.count(2) == 1:
            return('Full House')
        else:
            return('Three of a Kind')
    elif max(freak) == 4:
        return('Four of a Kind')

for x in range(20):
    print(hand_checker(hands_file[x]),hands_file[x])

#for m in hands_file:
    #for n in m:
        #if n = cant really change elements in the list i'm referring to
'''x = 0
while x<1001:
    hand1 = [[a[0],a[1]] for a in hands_file[2*x]]
    hand2 = [[a[0],a[1]] for a in hands_file[2*x+1]]
    print(hand1,hand2)
    x +=1 '''

    
   
    



'''def Rank(hand):
    frequencies = [[] for l in range(5)]
    for a in hand:'''
    

