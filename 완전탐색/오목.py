import sys
input = sys.stdin.readline
n = 19
board = [list(map(int, input().split())) for _ in range(n)]

visited = []

dx = [0,1,1,1]
dy = [1,1,0,-1]

def dfs(i,j, cnt, direction):
    value = board[i][j]
    nx = i + dx[direction]
    ny = j + dy[direction]
    visited.append((i,j,direction))

    if 0<=nx<n and 0<=ny<n and (nx, ny,direction) not in visited:
        if board[nx][ny]==value:
            cnt=dfs(nx,ny, cnt+1, direction)
    return cnt

for i in range(n):
    for j in range(n):
        if not board[i][j]==0:
            for d in range(4):
                if (i,j,d) not in visited:
                    if dfs(i, j, 1, d) == 5:
                        print(board[i][j])
                        if d == 3:
                            i,j = i+4,j-4
                        print(i+1,j+1)
                        exit()
print(0)