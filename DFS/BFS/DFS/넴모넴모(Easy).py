# 파이썬으로 하면 시간 초과 => PyPy3
n, m = map(int, input().split())

graph =[[0]*(m+1) for _ in range(n+1)]

ans = 0

def dfs(cnt):
    global ans
    if cnt == n*m:
        ans+=1
        return
    
    x = cnt//m+1
    y = cnt%m+1
    
    dfs(cnt+1)
    
    if graph[x-1][y] == 0 or graph[x][y-1]== 0 or graph[x-1][y-1]==0:
        graph[x][y] = 1
        dfs(cnt+1)
        graph[x][y] = 0
        
dfs(0)
print(ans)