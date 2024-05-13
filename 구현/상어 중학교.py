import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0,1,0,-1], [-1,0,1,0]

def find_group(x,y,visited):
    v = [[0]* n for _ in range(n)]
    
    rainbow, cnt = 0, 0
    queue = deque()
    queue.append((x,y))
    color = board[x][y]
    visited[x][y] = 1
    v[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        cnt+=1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]==color and not v[nx][ny]:
                    v[nx][ny] = 1
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                if board[nx][ny]==0 and not v[nx][ny]:
                    v[nx][ny] = 1
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                    rainbow+=1
    return rainbow, cnt

def gravity():
    for i in range(n):
        for j in range(n-2, -1, -1):
            if board[j][i]==-1 or board[j][i]==-2: continue
            tmp = j
            while True:
                if tmp+1==n: break
                if board[tmp+1][i] != -2: break
                tmp+=1
            color = board[j][i]
            board[j][i] = -2
            board[tmp][i] =color    
    return                
                
ans = 0
while True: # 오토 플레이
    # 블록 그룹이 존재하는 동안 반복!
    group = []
    visited = [[0] * n for _ in range(n)]
    
    # 블록 그룹: 같은 색의 일반 블록 하나 이상, 검은색 x
    # 기준 블록(일반 블록)을 찾아가면서 크기가 가장 큰 블록 그룹을 찾아야 함
    for i in range(n):
        for j in range(n):
            if board[i][j]>0 and board[i][j] and not visited[i][j]: # group에 해당 색의 그룹이 없다면
                rainbow, cnt = find_group(i,j, visited)
                if cnt>1:
                    group.append((cnt, rainbow, i, j))
    
    if not group: break # 블록이 존재하지 않으면, 그만!
    
    # 제거할 그룹 찾기
    group.sort(reverse= True)
    ans += group[0][0] **2
    remove = deque()
    remove.append((group[0][2],group[0][3]))
    color = board[group[0][2]][group[0][3]]
    board[group[0][2]][group[0][3]] = -2 # 제거 표시
    while remove:
        x, y = remove.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == color or board[nx][ny] ==0:
                    board[nx][ny] = -2
                    remove.append((nx,ny))
    # 중력!!
    gravity() 
    new = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[n-j-1][i] = board[i][j]
    board=new
    gravity()
    
    # print(board)    
    # print(ans)
    
print(ans)




