import sys
from collections import deque 
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
danji = []

dx, dy = [1,-1,0,0], [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    cnt = 1
    
    while queue:
        hx, hy = queue.popleft()
        for i in range(4):
            nx, ny = hx+dx[i], hy+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                    cnt+=1
                
    return cnt

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j]==1:
            danji.append(bfs(i,j))
            
print(len(danji))
danji.sort()
for i in danji:
    print(i)