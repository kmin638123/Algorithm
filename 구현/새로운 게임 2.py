import sys
input = sys.stdin.readline

n, k = map(int, input().split())
chess = [[0]*(n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]

game = [[[] for _ in range(n+1)] for _ in range(n+1)] # x,y 별로 말 저장
horse = [[] for _ in range(k)]

for i in range(k):
    x, y, d = map(int, input().split())
    game[x][y].append(i)
    horse[i] = [x,y,d]

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

# 0 흰색, 1 빨간색, 2 파란색
turn = 0

def white_red(x,y,nx,ny,i, color):
    idx = game[x][y].index(i)
    
    move = game[x][y][idx:] # 현재 말 위에 있는 말들
    for h in move:
        horse[h][0], horse[h][1] = nx,ny
    if color: # 빨간색
        move.reverse()
    game[nx][ny]+=move # 새로운 곳에 더해주기
    game[x][y]=game[x][y][:idx] # 기존 말 빼주기
    
    # 만약 새로 더한 곳의 말이 4개 이상이라면 게임 종료
    if len(game[nx][ny])>=4:
        return False
    return True

def blue(x,y,d,i):
    if d%2==1: d+=1
    else: d-=1
    
    horse[i][2] = d
    nx, ny = x+dx[d], y+dy[d]
    if not (1<=nx<=n and 1<=ny<=n):
        return True
    
    if chess[nx][ny]!=2:
        return white_red(x,y,nx,ny,i,chess[nx][ny])
    else:
        return True

while turn<=1000:
    turn+=1
    
    for i in range(k):
        hx, hy, d = horse[i]
        nx, ny = hx+dx[d], hy+dy[d]
        if not (1<=nx<=n and 1<=ny<=n): # 체스판을 벗어나는 경우, 방향만 바꿔줌
            # if d%2==1: d+=1
            # else: d-=1
            # horse[i][2] = d
            
            if not blue(hx,hy,d,i):
                print(turn)
                exit()
            
            # for row in game:
            #     print(row)
            
            # print(horse)
            continue
        
        if 0<=chess[nx][ny]<=1 : # 흰색
            horse[i] = [nx,ny,d]
            
            if not white_red(hx,hy,nx,ny,i, chess[nx][ny]):
                print(turn)
                exit()
        else: # 파란색   
            if not blue(hx,hy,d,i):
                print(turn)
                exit()
                
        # for row in game:
        #     print(row)
            
        # print(horse)

print(-1)