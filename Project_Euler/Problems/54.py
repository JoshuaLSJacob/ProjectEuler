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

'''print(hands_file[0])
print(sorted(hands_file[0], key = itemgetter(1)))'''

def frequency_checker(hand):
    z = [0 for m in range(14)]
    x = 0
    while x<5:
        z[hand[x][0]-1] += 1
        x += 1
    return(z)

def flush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return(True)

    
def hand_checker(hand):
    freak = frequency_checker(hand)
    if max(freak) == 1:
        if hand[0][0]+4==hand[4][0] or hand[3][0]== 5 and hand[4][0]-9 == 13:
            if flush(hand):
                print(hand,'straight flush')
                return([8,0,0])
                
            else:
                print(hand,'straight')
                return([4,0,0])
                

        elif flush(hand):
                print(hand,'flush')
                return([5,0,0])
                
        else:
            return([0,0,0])
            
    elif max(freak) == 2:
        if freak.count(2) == 2:
            return([2,13-freak[::-1].index(2),freak.index(2)])
            exit()
            
        else:
            return([1,freak.index(2),0])
    elif max(freak) == 3:
        if freak.count(2) == 1:
            return([6,freak.index(3),freak.index(2)])
        else:
            return([3,freak.index(3),0])
    elif max(freak) == 4:
        return([7,freak.index(4),0])

    
a = 0
b = 0
c = 0
r = 0


while r <1999:
    if hand_checker(hands_file[r]) == hand_checker(hands_file[r+1]):
        for x in range(5):
            if hands_file[r][-x-1][0] > hands_file[r+1][-x-1][0]:
                a += 1
                break
            elif hands_file[r][-x-1][0] < hands_file[r+1][-x-1][0]:
                b += 1
                break
            elif x == 4:
                c += 1
                print(hands_file[r], hands_file[r+1][-x][0],'happy')
                
    elif hand_checker(hands_file[r]) > hand_checker(hands_file[r+1]):
        a += 1
    else:
        b += 1
    r += 2

