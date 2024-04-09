# import sys
# input = sys.stdin.readline

# # print(ord("A"), ord("Z")) # 65, 90
# r, c = map(int, input().split())
# alpha = [list(input().rstrip()) for _ in range(r)]

# used = [False] * 26

# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

# used[ord(alpha[0][0])-65] = True
# ans = 0

# def dfs(x, y, cnt):
#     global ans
#     check = 0
#     for i in range(4):
#         nx, ny = x+dx[i], y+dy[i]
#         if 0<=nx<r and 0<=ny<c and not used[ord(alpha[nx][ny])-65]:
#             check = 1
#             used[ord(alpha[nx][ny])-65] = True
#             dfs(nx,ny, cnt+1)
#             used[ord(alpha[nx][ny])-65] = False
#     if not check:
#         ans = max(ans, cnt)

# dfs(0,0,1)

# print(ans)

#########################################################
# import sys
# input = sys.stdin.readline

# # print(ord("A"), ord("Z")) # 65, 90
# r, c = map(int, input().split())
# alpha = [list(input().rstrip()) for _ in range(r)]

# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

# ans = 0
# def dfs(x, y, used):
#     global ans
#     # check = 0
#     ans = max(ans, len(used))
#     for i in range(4):
#         nx, ny = x+dx[i], y+dy[i]
#         if 0<=nx<r and 0<=ny<c and alpha[nx][ny] not in used:
#             dfs(nx,ny, used+ alpha[nx][ny])
#     # if not check:
#     #     ans = max(ans, len(used))

# dfs(0,0,alpha[0][0])

# print(ans)

########################################################
# dfs로 하면 시간초과 뜨나봐,,, bfs로 어케 하지
import sys
input = sys.stdin.readline

# print(ord("A"), ord("Z")) # 65, 90
r, c = map(int, input().split())
alpha = [list(input().rstrip()) for _ in range(r)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i, j):
    ans = 0
    queue = set([(i,j, alpha[i][j])])
    while queue:
        x, y, path = queue.pop()
        ans = max(ans, len(path))
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and alpha[nx][ny] not in path:
                queue.add((nx,ny,path+alpha[nx][ny]))
            
    print(ans)
bfs(0,0)


