# 초기 아이디어: 이동할 수 있는 범위 내에서 쭉 이동하다가, 막히거나 목표 위치면 stop..
# 시간 초과 풀이
# import sys
# from collections import deque

# n, m, k = map(int, input().split())
# graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# x1, y1, x2, y2 = map(lambda x:x-1, list(map(int, input().split())))
# graph[x1][y1] = 0

# queue = deque()
# queue.append((x1,y1))

# def see(x,y, nx, ny):
#     for i in range(x,nx):
#         if graph[i][y]=="#":
#             return False
#     for j in range(y,ny):
#         if graph[x][j]=="#":
#             return False
            
#     return True

# while queue:
#     x, y = queue.popleft()
#     if x==x2 and y==y2:
#         print(graph[x][y])
#         break 
#     for i in range(1, k+1):
#         dx = [i,-i,0,0]
#         dy = [0,0,-i,i]
#         for j in range(4):
#             nx = x+dx[j]
#             ny = y+dy[j]
#             if 0<=nx<n and 0<=ny<m:
#                 if graph[nx][ny]=="." and see(x,y,nx,ny):
#                     # print((nx,ny))
#                     graph[nx][ny]=graph[x][y]+1
#                     queue.append((nx,ny))

# if graph[x2][y2]==".":
#     print(-1)
#################################################
# 다시 풀기!
# 연속적으로 이동할 수 있다는 조건에 의해 탐색 방향 순서에 따라 결과값이 달라질 수 있다!
# 따라서, 방문했던 길이라서 무조건 탐색을 멈추면 틀려버린다.
# 방문한 길이라도 그 칸을 건너뛰어서 같은 방향의 그 다음 칸을 탐색한다.

import sys
from collections import deque

n, m, k = map(int, input().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

x1, y1, x2, y2 = map(lambda x:x-1, list(map(int, input().split())))
graph[x1][y1] = 0

def bfs(x1,y1,x2,y2):
    queue = deque()
    queue.append((x1,y1))

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while queue:
        x, y = queue.popleft()
        if x==x2 and y==y2:
            return graph[x][y]
        for i in range(4):
            for j in range(1,k+1):
                nx = x+dx[i] * j 
                ny = y+dy[i] * j
                if 0<=nx<n and 0<=ny<m and not graph[nx][ny]=="#" :
                    if graph[nx][ny]==".": # 빈칸인 경우
                        graph[nx][ny]=graph[x][y]+1
                        queue.append((nx,ny))
                    elif graph[x][y]<graph[nx][ny]: #  그 다음 칸 (k+=1)
                        continue
                    #### 이 else break 안 쓰면 시간 초과 뜸!!!!! wtf
                    # 아마 그러면 graph[x][y]>=graph[nx][ny] 이겠지?
                    # 이 경우에는 break 하는 게 맞지 응...
                    else:
                        break
                else: # 벽을 마주치거나 범위 내에 있지 않은 경우 방향 바꾸기 (i 바꾸기)
                    break
            
    return -1

print(bfs(x1,y1,x2,y2))