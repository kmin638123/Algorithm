# 아기 상어
# 초기 아이디어: 물고기들의 위치를 찾는 함수를 정의한 후, 리스트로 결과 반환(각 물고기들과의 거리와 위치)
# 종료 조건문을 걸어 함수 반복 실행 (시간은 먹은 물고기들과의 거리의 총 합)
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


sx, sy = 0,0 # 처음 아기 상어 위치
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j
            # !! 아기 상어의 초기 위치는 좌표 저장 후, 0으로 초기화 해줘야 함!!
            graph[i][j] = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j, size): # 현재 아기상어의 위치, 크기가 input
    queue = deque()
    queue.append((i,j,0))
    
    fish = []
    visited = [[False] * n for _ in range(n)]
    while queue:
        x, y, d = queue.popleft()
        
        if 1<=graph[x][y]<size: # 먹을 수 있는 물고기가 있는 칸이면
            fish.append([x,y,d])
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if 0<=graph[nx][ny]<=size and not visited[nx][ny]:
                    # print((nx,ny, d+1))
                    queue.append((nx,ny,d+1))
                    visited[nx][ny]=True   
    
    return fish

size = 2 # 아기 상어 크기
time = 0 
eat = 0 
while True:
    fishes = bfs(sx,sy,size) #[위치, 거리] 형태
    # print(fishes)
    if len(fishes)==0: # 더 이상 잡아먹을 물고기 없음
        print(time)
        break
    
    # 제일 먼저 먹을 물고기의 거리를 더해줌!
    f = sorted(fishes, key= lambda x:(x[2],x[0],x[1]))[0]
    time += f[2] # 가까운 거리, 가장 위, 가장 왼쪽의 물고기 부터!
    # 아기 상어 위치 이동
    sx, sy = f[0], f[1]  
    # 물고기 잡아먹혀서 빈칸 됨!
    graph[f[0]][f[1]] = 0
    # 사이즈 커져야 하는지 체크
    eat +=1
    if eat==size:
        size+=1
        eat = 0           
            
            
######################################################
# 아기 상어2
from collections import deque
import copy
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

def dfs(i, j, graph):
    queue = deque()
    queue.append((i,j,-1))
    
    while queue:
        x, y, d = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    return -d
                elif graph[nx][ny]==0:
                    queue.append((nx,ny,d-1))
                    graph[nx][ny]=-1  

res = 0
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            copy_graph = copy.deepcopy(graph)
            tmp = dfs(i, j, copy_graph)
            # print(tmp)
            res = max(tmp, res)

print(res)