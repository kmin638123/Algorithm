n, m = map(int, input().split())
b = sorted(list(map(int, input().split())))
temp = []

def dfs(depth):
    if len(temp) == m:
        print(*temp)
        return
    else:
        for i in range(depth, n):
            temp.append(b[i])
            dfs(i+1)
            temp.pop()

dfs(0)