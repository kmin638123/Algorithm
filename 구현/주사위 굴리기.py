import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

order = list(map(int, input().split()))

dice = [0] * 7

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]


def roll(i):
    global dice
    if i == 1: # 동
        dice = [0, dice[3],dice[2],dice[6],dice[1],dice[5],dice[4]]
    elif i == 2: # 서
        dice = [0, dice[4],dice[2],dice[1],dice[6],dice[5],dice[3]]
    elif i == 3: # 북
        dice = [0, dice[2],dice[6],dice[3],dice[4],dice[1],dice[5]]
    else:
        dice = [0, dice[5],dice[1],dice[3],dice[4],dice[6],dice[2]]
        
    

for i in order:
    x += dx[i]
    y += dy[i]

    if not (0<=x<n and 0<=y<m):
        x -= dx[i]
        y -= dy[i]
        continue
    
    # 주사위 굴려!
    roll(i)
    
    value = graph[x][y]
    
    if value == 0: # 주사의 바닥면 graph에 복사
        graph[x][y] = dice[1]
    else:
        dice[1] = value
        graph[x][y] = 0
        
    print(dice[6])
    
    