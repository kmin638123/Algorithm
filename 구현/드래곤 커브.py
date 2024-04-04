import sys
input = sys.stdin.readline

n = int(input())
# dragons = [list(map(int, input().split())) for _ in range(n)]

# graph = [[False] * 100 for _ in range(100)]
points = set()

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def curve(dragon):
    end_x, end_y = dragon[-1][0], dragon[-1][1]
    for idx, point in enumerate(dragon[:-1]):
        x, y = point[0], point[1]
        dx, dy = x-end_x, y-end_y
        nx, ny = end_x+dy, end_y-dx
        points.add((nx,ny))
        
        # graph[nx][ny] = True
        if idx == 0:
            end = (nx, ny)
        else:
            dragon.append((nx, ny))
    dragon.append(end)
    # print(dragon)
        
for _ in range(n):
    y,x,d,g = map(int, input().split())
    dragon = [(x,y)]
    # graph[x][y] = True
    points.add((x,y))
    nx = x+dx[d]
    ny = y+dy[d]
    dragon.append((nx, ny))
    # graph[nx][ny] = True
    points.add((nx,ny))
        
    for _ in range(g):
        curve(dragon)


# print()
ans = 0 
graph = sorted(list(points))
for x, y in graph:
    if (x+1, y) in graph and (x+1,y+1) in graph and (x,y+1) in graph:
        ans+=1
        
print(ans)