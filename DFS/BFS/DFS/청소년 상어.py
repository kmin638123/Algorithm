import sys
from copy import deepcopy
input = sys.stdin.readline


f = [[] for _ in range(17)] # 각 물고기 별 정보!! index가 물고기 넘버; [x,y, 뱡향]
r = [[0] * 4 for _ in range(4)] # 위치 별 물고기 저장하는 배열

for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        num = row[j*2]
        direction = row[j*2+1]
        f[num]=[i,j,direction-1]
        r[i][j] = num

direction = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]


def dfs(sx, sy, f, r, eat): # 상어가 이동하는 위치, 방향, 상어가 먹은 물고기 번호
    global ans
    fish, room = deepcopy(f), deepcopy(r)
    sd = fish[room[sx][sy]][2]
    # 상어 이동!!
    if room[sx][sy]: # 물고기가 존재한다면 물고기 먹어라!
        fish[room[sx][sy]] = [] # 빈 리스트로 설정!
        room[sx][sy] = 0
    # print("sx,sy:"+str(sx), str(sy))
    # for row in room:
    #     print(*row)
        
    # 물고기 이동!!
    for i in range(1, 17): # 1부터 순서대로
        if fish[i]: # 물고기가 살아있다면, 이동해라~
            x, y, d = fish[i]
            # 이동할 수 있을 때까지 반시계 회전!
            # 한 바퀴 돌아도 회전할 수 없으면 이동하지 않음
            for j in range(8):
                nd = (d+j)%8
                nx, ny = x+direction[nd][0], y+direction[nd][1]
                # 이동할 수 없는 경우: 상어 있는 칸!
                if (nx,ny)==(sx,sy):
                    continue
                if not(0<=nx<4 and 0<=ny<4):
                    continue
                # 이동할 수 있는 경우: 빈 칸
                if room[nx][ny] == 0:
                    room[x][y] = 0
                # 다른 물고기가 있는 칸
                else:
                    other = room[nx][ny]
                    fish[other] = [x,y,fish[other][2]]
                    room[x][y] = other
                # 물고기 이동!    
                fish[i] = [nx,ny,nd] 
                room[nx][ny] = i
                break
    # print("finish")
    # for row in room:
    #     print(row)
    # 다음 이동
    while True:
        # 물고기 있는 칸으로 이동 가능
        sx+=direction[sd][0]
        sy+=direction[sd][1]
        if not(0<=sx<4 and 0<=sy<4): # 범위를 벗어나면?
            ans = max(ans, eat)
            return
        # 물고기가 존재하면 이동
        if room[sx][sy]:
            dfs(sx,sy,fish, room, eat+room[sx][sy])
        
ans = 0    
dfs(0,0, f,r, r[0][0])

print(ans)