import sys
input = sys.stdin.readline

t = int(input()) # 지폐
k = int(input()) # 동전 가지수

coins = [[0,0]]+[list(map(int, input().split())) for _ in range(k)]
dp = [[0] * (t+1) for _ in range(k+1)] # dp[i][j] : i번째 동전까지 사용해서 j원을 만드는 가지수

for i in range(k+1):
    dp[i][0] = 1

for i in range(1,k+1):
    coin, cnt = coins[i]
    for j in range(cnt+1): # i번째 coin을 j 번 사용했을 때, 해당 동전 안쓰는 경우 포함하려면 0도 무조건 포함해야 됨. 
        for value in range(t+1): # value 원을 만들 수 있는 경우의 수 계산
            new = value + coin * j
            if new == 0:
                continue
            if new < t+1:
                dp[i][new] += dp[i-1][value]
            else:
                break        
print(dp[k][t])