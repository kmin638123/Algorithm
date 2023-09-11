# virus
#
# from collections import deque
#
# n, m = [int(input()) for _ in range(2)]
# graph = [[] for _ in range(n+1)]
#
# for i in range(m):
#     fst, snd = map(int, input().split())
#     graph[fst].append(snd)
#     graph[snd].append(fst)
#
# visited = [False] * (n+1)
#
# def bfs(start):
#     queue = deque([start])
#     visited[start] = True
#
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#
# bfs(1)
#
# print(visited.count(True)-1)
############################################
# 특정 거리의 도시 찾기
#
# from collections import deque
# import sys
#
# n, m, k, x = map(int,sys.stdin.readline().split())
# graph = [[] for _ in range(n+1)]
#
# for i in range(m):
#     f, t = map(int,sys.stdin.readline().split())
#     graph[f].append(t)
#
# visited = [-1] * (n+1)
# visited[x] = 0
# def bfs(start):
#     queue = deque([start])
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if visited[i] == -1:
#                 visited[i] = visited[v]+1
#                 queue.append(i)
#
# bfs(x)
#
# if visited.count(k):
#     for i in range(1, n+1):
#         if visited[i] == k: print(i)
# else: print(-1)
##########################################
# 연구소
# import sys
# import copy
# from collections import deque
#
# n, m = map(int, sys.stdin.readline().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# def bfs():
#     global result
#     queue = deque()
#     temp = copy.deepcopy(graph)
#
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j]==2:
#                 queue.append((i,j))
#     while queue:
#         y, x = queue.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx>=0 and ny>=0 and ny<n and nx<m:
#                 if temp[ny][nx] == 0:
#                     temp[ny][nx] = 2
#                     queue.append((ny,nx))
#
#     count = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 count+=1
#     result = max(count, result)
#
# def wall(cnt):
#     if cnt == 3:
#         bfs()
#         return
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 wall(cnt+1)
#                 graph[i][j]=0
#
# result = 0
#
# wall(0)
# print(result)
# 시간 초과 풀이
##########################################
# from itertools import combinations
# import sys
# from collections import deque
# import copy
#
# n, m = map(int, sys.stdin.readline().split())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# safe = []
# virus = []
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# res = 0
#
# def bfs():
#     global res
#     cnt = len(safe)-3
#     queue = deque()
#     for x, y in virus:
#         queue.append((x,y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<m and tmp[nx][ny]==0:
#                 tmp[nx][ny] = 2
#                 queue.append((nx,ny))
#                 cnt -= 1
#     res = max(res, cnt)
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             safe.append((i,j))
#         elif graph[i][j] == 2:
#             virus.append((i,j))
#
# for comb in combinations(safe, 3):
#     tmp = copy.deepcopy(graph)
#     for x,y in comb:
#         tmp[x][y] = 1
#     bfs()
# print(res)
################################################
# 경쟁적 전염
# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().split())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# s, x, y = map(int, sys.stdin.readline().split())
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs():
#     que = []
#
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] != 0:
#                 que.append((graph[i][j],i,j,0))
#     que.sort() ## 맨 앞 요소로 정렬!
#     queue = deque(que)
#
#     while queue:
#         virus, x, y, sec = queue.popleft()
#         if sec == s:
#             return
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<n:
#                 if graph[nx][ny]==0:
#                     graph[nx][ny] = virus
#                     queue.append((graph[nx][ny],nx,ny,sec+1))
#
# bfs()
#
# print(graph[x-1][y-1])
################################################


