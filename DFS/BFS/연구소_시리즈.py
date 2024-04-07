# 연구소 => itertools 라이브러리 없이 구현해보기!

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

blank =[]
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            blank.append((i,j))
        elif arr[i][j] == 2:
            virus.append((i,j))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
 
def bfs():
    new = deepcopy(arr)
    safe = len(blank)-3
    queue = deque()
    
    for vx, vy in virus:
        queue.append((vx,vy))
        
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and new[nx][ny] == 0:
                new[nx][ny] = 2
                safe-=1      
                queue.append((nx,ny))
                                       
    return safe


def wall(idx):
    global ans
    if idx==3:
        safe = bfs()
        ans = max(ans, safe)
        return
    for i, j in blank:
        if arr[i][j] ==0:
            arr[i][j] = 1
            wall(idx+1)
            arr[i][j] = 0
        
ans = 0
wall(0)
print(ans)


###########################################
# 연구소 2
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

v = []
blank = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            v.append((i,j))
            arr[i][j] = 0
        elif arr[i][j] == 0:
            blank.append((i,j))


dx = [0,0,-1,1]
dy = [1,-1,0,0]
     
def bfs(virus):
    tmp = deepcopy(arr)
    b = len(blank) + len(v) - m # 빈칸 개수
    if b<=0:
        return 0
    
    queue = deque()
    for vx, vy in virus:
        queue.append((vx,vy,0))
        tmp[vx][vy] = 2
    
    while queue:
        x, y, cnt = queue.popleft()    
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and tmp[nx][ny]==0:
                tmp[nx][ny] = 2
                queue.append((nx,ny,cnt+1))
                b -= 1
                if b==0: return cnt+1
    return -1

def virus(cnt,varr):
    global ans
    if len(varr) == m:
        time = bfs(varr)
        if time == -1:
            return
        ans = min(ans, time)
        return
    for i in range(cnt, len(v)):
        virus(i+1,varr+[(v[i][0],v[i][1])])
    
    
ans = 2500
virus(0,[])
print(ans if ans!=2500 else -1)

###########################################
# 연구소 3
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

v = []
blank = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            v.append((i,j))
            arr[i][j]= -1
        elif arr[i][j] == 0:
            blank.append((i,j))


dx = [0,0,-1,1]
dy = [1,-1,0,0]
     
def bfs(virus):
    tmp = deepcopy(arr)
    b = len(blank) # 빈칸 개수
    if b<=0:
        return 0
    
    queue = deque()
    for vx, vy in virus:
        queue.append((vx,vy,0))
        tmp[vx][vy] = 2
    
    while queue:
        x, y, cnt = queue.popleft()    
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if tmp[nx][ny]==0:
                    tmp[nx][ny] = 2
                    queue.append((nx,ny,cnt+1))
                    b -= 1
                    if b==0: return cnt+1
                if tmp[nx][ny] == -1: # 비활성 바이러스
                    tmp[nx][ny] = 2
                    queue.append((nx,ny,cnt+1))
                    
    return -1

def virus(cnt,varr):
    global ans
    if len(varr) == m:
        time = bfs(varr)
        if time == -1:
            return
        ans = min(ans, time)
        return
    for i in range(cnt, len(v)):
        virus(i+1,varr+[(v[i][0],v[i][1])])
    
    
ans = 2500
virus(0,[])
print(ans if ans!=2500 else -1)