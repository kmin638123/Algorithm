# 단 검을 주웠을 때! 들렸던 곳을 또 들려도 된다.
import sys
from collections import deque

input = sys.stdin.readline

n, m, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
queue.append((0,0)) #용사 위치
visited = [[0]*m for _ in range(n)]
dx, dy = [0,1,0,-1], [1,0,-1,0]

visited[0][0] = 1
gram = 10001

while queue:
    x, y = queue.popleft()
    if castle[x][y] == 2: # 단검 줍!
        gram = abs(n-1-x)+abs(m-1-y) +visited[x][y]-1
    
    if x==n-1 and y==m-1: # 공주 구출 성공~
        t = min(visited[x][y]-1, gram)
        if t>T: print("Fail")
        else: print(t)
        exit()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and castle[nx][ny]!=1:
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
     
print("Fail") if gram>T else print(gram)