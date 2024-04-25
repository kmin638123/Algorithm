import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = deque(list(map(int, input().split())))

zero,step = 0,0
for i in a:
    if i == 0:
        zero+=1

belt = deque([False] * n) # 해당 칸의 로봇 여부
while True:
    if zero>=k:
        break

    # 벨트가 로봇과 함께 한 칸 회전
    belt.rotate(1)
    a.rotate(1)
    
    # 내리는 칸에 도착하면 즉시 내림
    belt[n-1] = False 
    
    # 로봇 한 칸 더 회전 (n-1번째 칸부터 1번째 칸까지 확인)
    # 이동하려는 칸에 로봇이 없으며, 내구도가 1 이상!
    for i in range(n-2,-1,-1):
        if belt[i] and not belt[i+1]: # i번째 칸에 로봇이 있고, 다음 칸에는 없음
            if a[i+1]>0: # 이동하려는 칸의 내구도가 1 이상이어야 함
                belt[i], belt[i+1] = False, True
                a[i+1]-=1
                if a[i+1]==0:
                    zero+=1
    
    # 내리는 칸에 도착하면 즉시 내림
    belt[n-1] = False             
    
    # 올리는 위치에 로봇 올림
    if a[0]>0:
        belt[0] = True
        a[0]-=1
        if a[0]==0:
            zero+=1
    
    step+=1

print(step)