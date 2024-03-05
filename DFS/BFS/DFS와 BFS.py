from collections import deque

n, m, v = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in edges:
    i.sort()
    
def dfs(start):
    visited[start]=True
    print(start, end=" ")
    for i in edges[start]:
        if not visited[i]:
            dfs(i)


def bfs():
    queue = deque()
    queue.append(v)
    visited[v] = True
    
    while queue:
        n = queue.popleft()
        print(n, end=" ")
        
        for i in edges[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs()