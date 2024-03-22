import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

rx, ry, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while True:
    if room[rx][ry]==0:
        room[rx][ry]=2
        cnt+=1
    clean = 0
    for i in range(1,5):
        if room[rx+dx[(d+4-i)%4]][ry+dy[(d+4-i)%4]]==0:
            d = (d+4-i)%4
            rx, ry = rx+dx[d],ry+dy[d]
            clean = 1
            break
    if not clean: # 청소되지 않은 빈칸이 없는 경우
        if room[rx-dx[d]][ry-dy[d]]==1:
            print(cnt)
            exit()
        else:
            rx, ry = rx-dx[d], ry-dy[d]
    
        