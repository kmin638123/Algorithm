import sys
input = sys.stdin.readline

n, m = map(int, input().split())

poketmon = dict()

for i in range(n):
    poketmon[i+1] = input().rstrip()
    
num = {v:k for k,v in poketmon.items()}

for _ in range(m):
    q = input().rstrip()
    if not q.isdigit():
        print(num[q])
    else:
        print(poketmon[int(q)])
    
