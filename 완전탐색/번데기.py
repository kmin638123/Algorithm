a = int(input())
t = int(input())
bd = int(input())

p = [] 

bbun, degi = 1, 1
n = 0

while True:
    tmp = bbun
    n +=1
    for _ in range(2):
        p.append((0, bbun))
        bbun+=1
        p.append((1, degi))
        degi+=1
    for _ in range(n+1):
        p.append((0,bbun))
        bbun+=1
    for _ in range(n+1):
        p.append((1, degi))
        degi+=1
    if tmp<t<=bbun:
        print(p.index((bd, t))%a)
        break