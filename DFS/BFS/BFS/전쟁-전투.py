from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]

visited = [[False] * n for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

W = 0
B = 0

def bfs(i,j):
    team = graph[i][j]
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    cnt = 1
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[ny][nx]==team and not visited[ny][nx]:
                    queue.append((ny,nx))
                    cnt += 1
                    visited[ny][nx]=True  

    return cnt

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j]=="W":
                W+=(bfs(i,j)**2)
            else:
                B+=(bfs(i,j)**2)

print(W, end=" ")
print(B)       
