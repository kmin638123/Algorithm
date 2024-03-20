# 동전 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [0] * (k+1)

for coin in coins:
    for i in range(1, k+1):
        if i<coin:
            continue
        if i == coin:
            dp[i]+=1
        else:
            dp[i]+=dp[i-coin]
        
print(dp[-1])
            
##########################################
# 동전 2
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [1e9] * (k+1)

for coin in coins:
    for i in range(1, k+1):
        if i<coin:
            continue
        if i == coin:
            dp[i] = min(dp[i],1)
        else:
            dp[i] = min(dp[i-coin]+1,dp[i])

ans = dp[-1] if dp[-1]!=1e9 else -1
print(ans)