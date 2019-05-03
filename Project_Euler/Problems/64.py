num = 10
def set_up(num):
    root = 1
    counter = 1
    while root**2 < num:
        root+=1
    root -= 1

    a = root
    b = num - a**2

    while counter*b <= a + root:
        counter += 1

    counter -= 1

    return(a,b,counter,num,root)


def next_a(a,b,counter):
    return counter*b-a

def next_b(num,a,b):
    return (num-a**2)/b

def next_counter(a,b,root):
    count = 1
    while count*b <= a+ root:
        count += 1
    return count-1

def next_counter_whole(a,b,counter,num,root):
    a = next_a(a,b, counter)
    b = next_b(num,a,b)
    counter = next_counter(a,b,root)
    return a,b,counter

def period_finder(num):
    period = 0
    a,b,counter,num,root = set_up(num)
    starter = (a,b,counter)
    period += 1
    a,b,counter = next_counter_whole(a,b,counter,num,root)
    while (a,b,counter) != starter:
        period += 1
        a,b,counter = next_counter_whole(a,b,counter,num,root)
    return period


n = 2
odds = 0
while n <= 10000:
    if period_finder(n)% 2 == 1:
        odds += 1
    n += 1
print(odds)
