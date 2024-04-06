# 시간 초과 풀이
# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# r, c, t = map(int, input().split())

# room = []

# air = 0 # 공청 1st 열
# dirt = defaultdict(int)

# for i in range(r):
#     row = list(map(int, input().split()))
#     if row[0] == -1 and air == 0:
#         air = i
#     for j in range(c):
#         if 0<row[j]:
#             dirt[(i,j)] = row[j]
#             # dirt.append((i,j, row[j]//5))



# def spread():
#     dx = [0,0,-1,1]
#     dy = [1,-1,0,0]    
#     new = defaultdict(int)
#     for x,y in dirt.keys():
#         cnt = 0
#         for j in range(4):
#             nx, ny = x+dx[j], y+dy[j]
#             if 0<=nx<r and 0<=ny<c and (nx,ny) not in [(air,0), (air+1,0)]:
#                 cnt += 1
#                 if (nx,ny) not in new.keys(): # 새로운 칸에 확산
#                     new[(nx,ny)] = dirt[(x,y)] // 5
#                 else: # 있다면 더해줘야 하는데, 기존의 값은 지켜줘야 됨.
#                     new[(nx,ny)] += dirt[(x,y)] // 5
                    
#         remain = dirt[(x,y)] - (dirt[(x,y)]//5) * cnt
#         if (x,y) not in new.keys():
#             new[(x,y)] = remain
#         else:
#             new[(x,y)] += remain
#     return new

# def up():
#     dx = [0, -1, 0, 1]
#     dy = [1, 0, -1, 0]
#     direct = 0
#     before = 0
#     x, y = air, 1
#     while True:
#         nx = x + dx[direct]
#         ny = y + dy[direct]
#         if x == air and y == 0:
#             break
#         if nx < 0 or nx >= r or ny < 0 or ny >= c:
#             direct += 1
#             continue
#         dirt[(x,y)], before = before, dirt[(x,y)]
#         x = nx
#         y = ny
        
# # 공기청정기 아래쪽 이동
# def down():
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     direct = 0
#     before = 0
#     x, y = air+1, 1
#     while True:
#         nx = x + dx[direct]
#         ny = y + dy[direct]
#         if x == air+1 and y == 0:
#             break
#         if nx < 0 or nx >= r or ny < 0 or ny >= c:
#             direct += 1
#             continue
#         dirt[(x,y)], before = before, dirt[(x,y)]
#         x = nx
#         y = ny
    

# for _ in range(t):
#     # 확산; 확산되는 미세먼지의 양은 기존의 양을 기준으로 함.
#     dirt = spread()
    
#     # 순환
#     up()
#     down()
            
#     dirt[(air,1)] = 0
#     dirt[(air+1,1)] = 0

# ans = 0
# print(sum(dirt.values()))

###########################################
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

up, down = 0,0
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i+1
        break


def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    new = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y]==0 or arr[x][y]==-1:
                continue
            cnt = 0
            for j in range(4):
                nx, ny = x+dx[j], y+dy[j]
                if 0<=nx<r and 0<=ny<c and (nx,ny) not in [(up,0), (down,0)]:
                    cnt += 1
                    new[nx][ny] += arr[x][y] // 5
                    
            remain = arr[x][y] - (arr[x][y]//5) * cnt
            new[x][y] += remain
    return new


for _ in range(t):
    # 확산; 확산되는 미세먼지의 양은 기존의 양을 기준으로 함.
    arr = spread()
    
    # 순환
    air_up()
    air_down()
  

ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            ans += arr[i][j]
            
print(ans)