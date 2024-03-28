import sys
input = sys.stdin.readline

n, k = map(int, input().split())
obj = [(0,0)]

for _ in range(n):
    obj.append(list(map(int, input().split())))

dp = [[0] * (k+1) for _ in range(n+1)] # dp[n][k] = n번째 물건까지 담았을 때, 무게 k 배낭의 최대 가치

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = obj[i][0], obj[i][1]
        
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
            
print(dp[n][k])