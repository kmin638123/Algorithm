import sys
input = sys.stdin.readline

n = int(input())

s = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)

for i in range(n):
    dp[i+1] = max(dp[i+1],dp[i]) # 이전까지 수익과, 현재의 수익 비교
    if i+s[i][0]<=n:
        dp[i+s[i][0]]=max(dp[i+s[i][0]], dp[i]+s[i][1])
        
print(dp[-1])