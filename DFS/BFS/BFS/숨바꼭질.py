# 다시 풀어보기!!!
from collections import deque

n, k = map(int, input().split())


dist = [0] * (100001)

def bfs():
    queue = deque()
    queue.append(n)
    
    while queue:
        x = queue.popleft()
        if x==k:
            print(dist[x])
            return
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=100000 and not dist[nx]:
                dist[nx]=dist[x]+1
                queue.append(nx)

bfs()