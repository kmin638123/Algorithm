import sys
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

blank = 0
cctv = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            blank+=1
        elif 1<=graph[i][j]<=5:
            cctv.append((graph[i][j], i,j))
ans = 64
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(idx, visited):
    global ans
    if idx == len(cctv):
        # print(visited)
        ans = min(blank-len(visited), ans)
        return
    
    num, x, y = cctv[idx]
    
    d = [[i] for i in range(4)]
    if num== 2: d = [(i,i+2) for i in range(2)]
    if num==3: d = [(3,0),(1,0),(1,2),(3,2)]
    if num==4: d = [(1,2,3),(0,1,2),(0,1,3),(0,2,3)]
    if num==5: d = [(0,1,2,3)]
    
    for i in range(len(d)):
        tmp = deepcopy(visited)
        nx, ny = x, y
        while True :
            nx += dx[d[i][0]]
            ny += dy[d[i][0]]
            if not (0<=nx<n and 0<=ny<m) or graph[nx][ny] == 6:
                break
            if (nx, ny) not in tmp and graph[nx][ny]==0:
                tmp.append((nx, ny))
        
        if num!=1:
            nx, ny = x, y
            while True:
                nx += dx[d[i][1]]
                ny += dy[d[i][1]]
                if not (0<=nx<n and 0<=ny<m) or graph[nx][ny] == 6:
                    break
                if (nx, ny) not in tmp and graph[nx][ny]==0:
                    tmp.append((nx, ny))
            if num >= 4:
                nx, ny = x, y
                while True:
                    nx += dx[d[i][2]]
                    ny += dy[d[i][2]]
                    if not (0<=nx<n and 0<=ny<m) or graph[nx][ny] == 6:
                        break
                    if (nx, ny) not in tmp and graph[nx][ny]==0:
                        tmp.append((nx, ny))
                if num == 5:
                    nx, ny = x, y
                    while True:
                        nx += dx[d[i][3]]
                        ny += dy[d[i][3]]
                        if not (0<=nx<n and 0<=ny<m) or graph[nx][ny] == 6:
                            break
                        if (nx, ny) not in tmp and graph[nx][ny]==0:
                            tmp.append((nx, ny))
                
        dfs(idx+1,tmp)
 
dfs(0, [])
print(ans)
