from collections import deque

n = int(input())
e = int(input())

edges = [[] for _ in range(n+1)]

for _ in range(e):
    a, b= map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

queue = deque()
queue.append(1)

visited = [False] * (n+1)
visited[1]= True
cnt = 0
while queue:
    c = queue.popleft()
    for i in edges[c]:
        if not visited[i]:
            cnt+=1
            visited[i] = True
            queue.append(i)

print(cnt)