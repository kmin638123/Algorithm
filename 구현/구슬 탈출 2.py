import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())


board = blue = red = o = []

for i in range(n):
    line = list(input().rstrip())
    for j in range(m):
        if line[j]=="B": 
            blue = [i,j]
            line[j] = "."
        elif line[j]=="R": 
            red = [i,j]
            line[j] ="."
        elif line[j]=="O": o = [i,j]
    board.append(line)
        
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def move(d, b, r):
    cnt = check = 0
    blue, red = b,r
    rx, ry = red[0], red[1]
    while True:
        
        bx, by = blue[0]+dx[d], blue[1]+dy[d]
        if not check:
            rx, ry = red[0]+dx[d],red[1]+dy[d]
        
        if board[bx][by]== "#":
            bx, by = blue[0], blue[1]
        if board[rx][ry] =="#":
            rx, ry = red[0], red[1]
        
        if bx==rx and by==ry: # 구슬 두 개의 위치가 겹쳤을 때!
            bx, by = blue[0], blue[1]
            rx, ry = red[0], red[1]
            break
            
        if bx == o[0] and by==o[1]: # 파란 구슬이 먼저 구멍으로 갔을 경우
            return [0, [bx,by], [rx,ry]]

        if rx == o[0] and ry==o[1]:
            check = 1
            rx = ry = 0
        
        if blue == [bx,by] and red==[rx,ry]: # 두 구슬 모두 안 움직인 경우
            break
        blue = [bx,by]
        red = [rx, ry]
        cnt+=1
        
    if not cnt: # 두 구슬이 모두 움직이지 않은 경우
        return [0, [bx,by], [rx,ry]]
    if check:
        return [2, [bx, by], [rx,ry]]
    
    return [1, [bx,by], [rx,ry]]

            
ans = 0
queue = deque()
queue.append((red, blue, ans))

visited = []
visited.append((red,blue))

while queue:
    r, b, cnt = queue.popleft()
    # print(r,b,cnt)
    if cnt>=10:
        print(-1)
        exit()
        
    for i in range(4):
        tmp = move(i, b, r)
        if tmp[0]==1: # 빨간 구슬이 움직임!
            nb, nr = tmp[1], tmp[2]
            # print("move!")
            if (nr, nb) not in visited:
                # print(nb, nr, i, cnt+1)
                queue.append((nr, nb, cnt+1))
        elif tmp[0]==2: # 빨간 구슬이 구멍으로!
            # print("finish!")
            print(cnt+1)
            exit()

print(-1)