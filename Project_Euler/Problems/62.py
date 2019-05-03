baggage = [[1]]
d = 2
limit = 10000
while d < limit:
    if len(str((d-1)**3)) < len(str(d**3)):
        baggage = [[1]]
    a = 0
    while a < len(baggage):
        click = False
        if sorted(str(d**3)) in baggage[a]:
            baggage[a].append(d**3)
            click = True
            if len(baggage[a]) == 6:
                print baggage[a]
                d = limit
            a = len(baggage)
        a += 1
    if not click:
        baggage.append([sorted(str(d**3)),d**3])
    d += 1
    
