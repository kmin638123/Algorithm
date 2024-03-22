# from copy import deepcopy
# from itertools import combinations
# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(n)]

# house = []
# ch = []

# for i in range(n):
#     for j in range(n):
#         if city[i][j] == 1:
#             house.append((i,j))
#         elif city[i][j] == 2:
#             ch.append((i,j))

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# def bfs(hx,hy):
#     queue = deque()
    
#     queue.append((hx, hy,0))
#     ans = 1e9
#     visited = [[False]* n for _ in range(n)]
    
#     while queue:
#         x, y, cnt = queue.popleft()
#         # print((x,y,cnt))
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
            
#             if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
#                 queue.append((nx,ny,cnt+1))
#                 visited[nx][ny] = True
#                 if graph[nx][ny]==2:
#                     ans = min(cnt+1, ans)

#     return ans
# ans = 1e9
# for comb in combinations(ch, len(ch)-m):
#     graph = deepcopy(city)
#     for i, j in comb:
#         graph[i][j] = 0
#     dist = 0
#     for hx, hy in house:
#         # print()
#         dist += bfs(hx, hy)
#     ans = min(ans, dist)
    
# print(ans)
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
ch = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            ch.append((i,j))

ans = 1e9
for comb in combinations(ch, m):
    tmp = 0
    for hx, hy in house:
        dist = 1e9
        for x, y in comb:
            dist = min(abs(hx-x)+abs(hy-y),dist)
        tmp+=dist
    ans =min(tmp,ans)
    
print(ans)