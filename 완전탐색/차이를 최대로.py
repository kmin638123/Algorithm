import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0
def dfs(arr):
    global ans
    if len(arr) == n:
        s = sum(list(abs(a[arr[i]]-a[arr[i-1]]) for i in range(1,n)))
        ans = max(ans, s)
        return 

    for i in range(n):
        if i not in arr:
            dfs(arr+[i])    

for i in range(n):
    dfs([i])
    
print(ans)