from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j):
    
    queue = deque()
    queue.append((i,j))
    
    while queue:
        x, y = queue.popleft()
        if x==n-1 and y==m-1:
            return graph[x][y]
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    queue.append((nx,ny))
                    graph[nx][ny]+=graph[x][y]

print(bfs(0,0))