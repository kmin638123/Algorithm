import sys
from collections import deque
input = sys.stdin.readline

r,c,n = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]

bomb = deque()
# new_bomb = deque()
# 1초
if n == 1:
    for row in arr:
        print("".join(row))
    exit()
    
# 2초
for i in range(r):
    for j in range(c):
        if arr[i][j] == "O":
            bomb.append((i,j))
        else:
            arr[i][j] ="O"
            # new_bomb.append((i,j))
if n == 2:
    for row in arr:
        print("".join(row))
    exit()            

dx, dy= [1,-1,0,0], [0,0,-1,1]

if n%2==1:
    for idx in range((n-1)//2):
        visited = [[0]*c for _ in range(r)]
        while bomb:
            x, y= bomb.popleft()
            arr[x][y]="."
            visited[x][y] = 1
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                    arr[nx][ny]="."
                    visited[nx][ny] =1

        if idx == (n-3)//2:
            continue               
        bomb =deque()
        for i in range(r):
            for j in range(c):
                if not visited[i][j]:
                    bomb.append((i,j))
                arr[i][j] = "O"
        

for row in arr:
    print("".join(row))