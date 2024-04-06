import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    
    people = [(i,j)]
    tot = a[i][j]
    
    while queue:
        x, y= queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if l<=abs(a[nx][ny]-a[x][y])<=r:
                    people.append((nx,ny))
                    tot+=a[nx][ny]
                    queue.append((nx,ny))
                    visited[nx][ny] = True

    new = tot//len(people)
    for x,y in people:
        a[x][y] = new
    
    return True if len(people)>1 else False 
    
    
day = 0
while True:
    visited = [[False] * n for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j):
                    check = True
    
    if not check:
        break
    day+=1

print(day)