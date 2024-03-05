from collections import deque

n, m, k = map(int, input().split())
trash=[]

for _ in range(k):
    a, b= map(int, input().split())
    trash.append((a-1,b-1))
    
size = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and (nx,ny) in trash:
                if (nx,ny) not in visited:
                    queue.append((nx,ny))
                    cnt+=1
                    visited.append((nx,ny))
    return cnt
            
visited = []
for i, j in trash:
    if (i,j) not in visited:
        visited.append((i,j))
        s = bfs(i,j)
        size = max(s, size)
print(size)