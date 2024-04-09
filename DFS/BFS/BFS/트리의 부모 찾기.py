import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nodes =[[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
# print(nodes)

queue = deque()
queue.append(1) # 루트!

ans = [0] * (n+1)

while queue:
    parent = queue.popleft()
    
    for child in nodes[parent]:
        if ans[child]==0:
            ans[child] = parent
            queue.append(child)
            
for i in range(2, n+1):
    print(ans[i])