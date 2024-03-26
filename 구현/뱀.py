import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

# board = [[0] * n for _ in range(n)]
apple = []
for _ in range(k):
    ax, ay = map(int, input().split())
    # board[ax-1][ay-1] = 1
    apple.append([ax-1,ay-1])

l = int(input())
change = dict()
for _ in range(l):
    t, d = input().split()
    change[int(t)] = d
    
time = sx = sy = 0 
snake = deque()
snake.append((0,0))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

d = 0 # 현재 방향

while True:
    # print(time, snake)
    if time in change.keys():
        direction = change[time]
        if direction == "L":
            d = ((d-1)+4)%4
        else:
            d = (d+1)%4
            
    sx+= dx[d]
    sy+=dy[d]
    if not (0<=sx<n and 0<=sy<n):
        print(time+1)
        exit()
    if (sx,sy) in snake:
        print(time+1)
        exit()
    # if board[sx][sy]== 1:
    #     board[sy][sy] = 0 
    if [sx,sy] in apple:
        apple.remove([sx,sy])
    else:
        snake.popleft()
    snake.append((sx,sy))
    time+=1