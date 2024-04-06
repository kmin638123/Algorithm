import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())

shark = [list(map(int, input().split())) for _ in range(m)] # x, y, 속력, 방향, 크기

die = [False] * m # 잡아 먹혔는지 표시
dx = [-1,1,0,0]
dy = [0,0,1,-1]

ans = 0

def moving(j, move):
    x, y, s, d, z= shark[j]
    for k in range(s): # s만큼 이동해야 됨!
        if not (1<= x + dx[d-1] <=r and 1<= y + dy[d-1] <=c): # 방향 바꾸기
            dd = 1 if d%2 ==1 else -1
            d += dd
        x += dx[d-1]
        y += dy[d-1]
    shark[j] = [x,y,s,d,z]
            
    if (x,y) in move.keys(): # 한 칸에 상어 이미 존재
        if move[(x,y)][0]<z: # 지금 상어가 더 큼
            die[move[(x,y)][1]] = True # 기존 상어는 잡아 먹힘 
            move[(x,y)] = (z,j)
        else:
            die[j] = True # 지금 상어 잡아먹힘
    else:
        move[(x,y)] = (z,j)

for i in range(1, c+1): # 낚시왕이 1~c를 오른쪽까지 이동
    fish = {} # 같은 열에 있는 상어 저장 
    move = {} # 이동하는 상어의 위치 임시 저장; 위치: (사이즈, 계수)
    for j in range(m):
        if die[j]: # 잡아먹힘
            continue
        elif shark[j][1]==i: # 같은 열에 상어 있음!
            fish[j] = shark[j]
            # fish.append(shark[j])
        else: # 나머지 상어들은 이동시켜!
            moving(j, move)
        
    if fish: # 같은 열에 상어 존재
        fish = sorted(fish.items(), key= lambda x: x[1][0])
        die[fish[0][0]] = True # 잡아먹힘
        ans += fish[0][1][4]
        for j in range(1, len(fish)): # 나머지 상어들 이동시켜!
            moving(fish[j][0], move)


print(ans)      
    