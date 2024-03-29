# 시간초과 풀이
# import sys 
# input = sys.stdin.readline

# n, m = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(n)]
         
# value = []

# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

# def dfs(stk):
    
#     if len(stk) == 4:
#         if stk not in value:
#             # print(stk)
#             value.append(set(stk))
#         # value = max(value,sum(blocks))
#         return
#     for block in stk:
#         x, y = block
#         for idx in range(4):
#             nx = x+dx[idx]
#             ny = y+dy[idx]
#             if 0<=nx<n and 0<=ny<m and (nx,ny) not in stk:
#                 stk.append((nx,ny))
#                 dfs(stk)
#                 stk.pop()

# for i in range(n):
#     for j in range(m):
#         stk = []
#         stk.append((i,j))
#         dfs(stk)

# ans = 0
# for tetro in value:
#     tmp = 0
#     for x, y in tetro:
#        tmp+=graph[x][y]
#     ans = max(ans,tmp) 
            
# print(ans)

#####################################################
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
         
value =0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x,y,idx, tot):
    global value
    if value >= tot + max_val * (3 - idx): # 남은 블럭의 개수만큼 최대값을 더해줬을 때
        return
    if idx == 3:
            # print(stk)
        value = max(value, tot)
        return
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if idx==1:
                visited[nx][ny]=True
                dfs(x,y,idx+1,tot+graph[nx][ny])
                visited[nx][ny]=False
                
            visited[nx][ny]=True
            dfs(nx,ny,idx+1, tot+graph[nx][ny])
            visited[nx][ny]=False
    
max_val = max(map(max, graph)) # 2차원 그래프에서 최댓값 찾음!      
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,0, graph[i][j])
        visited[i][j] = False
        

print(value)