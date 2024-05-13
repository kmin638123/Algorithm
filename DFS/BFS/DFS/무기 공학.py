import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y, val):
    global ans
    
    if y==m:
        x, y = x+1, 0
    
    if x==n:
        ans = max(ans, val)
        return 
    nx, ny = x, y+1
    
    if not visited[x][y]:
        for i in range(4):
            x1, y1, x2, y2 = boomerang[i]
            nx1, ny1, nx2, ny2 = x+x1, y+y1, x+x2, y+y2
            if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m:
                if not visited[nx1][ny1] and not visited[nx2][ny2]:
                    visited[x][y] = visited[nx1][ny1] = visited[nx2][ny2] = 1
                    dfs(nx, ny, val+tree[x][y]*2+tree[nx1][ny1]+tree[nx2][ny2])
                    visited[x][y] = visited[nx1][ny1] = visited[nx2][ny2] = 0
    
    dfs(nx,ny,val)                    
        


visited = [[0] * m for _ in range(n)]
boomerang = [(0,-1,1,0),(0,-1,-1,0),(-1,0,0,1),(1,0,0,1)]
ans = 0

dfs(0,0,0)
print(ans)
