import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] *n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j==0:
            dp[i][j]=1
        if i==j==n-1:
            break
        nx = i+graph[i][j]
        ny = j+graph[i][j]
        
        if nx<n: dp[nx][j]+=dp[i][j]
        if ny<n: dp[i][ny]+=dp[i][j]

# print(dp)    
print(dp[n-1][n-1])