import sys
input = sys.stdin.readline

n = int(input())

town = []

tot = 0
for i in range(n):
    x, a = map(int, input().split())
    tot+=a
    if a != 0:
        town.append((x,a))
    
town.sort()
s = 0
for x, a in town:
    s+=a
    if s>= (tot+1)//2: ### tot//2 로 하면 안됨. 홀수일 경우 절반이 안될 수도 있기 때문에
        print(x)
        exit()