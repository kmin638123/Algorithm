# 파이썬으로는 시간초과,,, => 해결 방법 못 찾음

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

friend = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[b].append(a)
def hacking(idx):
    queue = deque()
    queue.append(idx)
    visited = [0] *(n+1)
    cnt = 0
    visited[idx] = 1
    while queue:
        com = queue.popleft()
        for i in friend[com]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                cnt+=1
    return cnt

ans = 0
computers = []

for i in range(1,n+1):
    num = hacking(i)
    if ans == num:
        computers.append(i)
    elif ans<num:
        ans = num
        computers = [i]
    # print(computers)  
        
print(*computers)