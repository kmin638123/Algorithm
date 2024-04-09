import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

sx, sy = 0,0

for i in range(n):
    row = list(map(lambda x:x*-1, list(map(int, input().split()))))
    for j in range(m):
        if row[j]==-2:
            sx, sy= i,j
    arr.append(row)
    
queue = deque()

queue.append((sx,sy, -2))
dx, dy= [0,0,-1,1],[1,-1,0,0]
while queue:
    x, y, d = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==-1:
            if d==-2: d=0
            arr[nx][ny] = d+1
            queue.append((nx,ny,d+1))
arr[sx][sy] = 0            
for row in arr:
    print(*row)