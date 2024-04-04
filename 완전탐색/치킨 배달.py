from itertools import combinations
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house, chicken =[], []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

dx = [0,1,0,-1]
dy = [1,0,-1,0]      

ans = 1e9                    
for comb in combinations(chicken, m):
    tmp = 0
    for hx, hy in house:
        dist = 1e9
        for cx, cy in comb:
            dist = min(abs(hx-cx)+abs(hy-cy), dist)
        tmp+=dist
        
    ans = min(tmp, ans)
    
print(ans)