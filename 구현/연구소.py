from copy import deepcopy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

blank = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            blank.append((i,j))
        elif graph[i][j]==2:
            virus.append((i,j))
safe = len(blank)-3

dx = [1,-1,0,0]            
dy = [0,0,-1,1]
            
def bfs(tmp):
    queue = deque()
    for i, j in virus:
        queue.append((i,j))
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny]==0:
                tmp[nx][ny]=2
                queue.append((nx,ny))
                cnt+=1
    return cnt
    
ans = n*m            
for comb in combinations(blank, 3):
    tmp = deepcopy(graph)
    for i, j in comb:
        tmp[i][j] = 1
        
    virus_cnt = bfs(tmp)
    ans = min(ans, virus_cnt)
    
print(safe-ans)