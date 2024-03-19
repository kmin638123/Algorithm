import sys
input = sys.stdin.readline

n = int(input())

s = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+s[i][0],n+1):
        if dp[j] < dp[i] +s[i][1]:
            dp[j] = dp[i]+s[i][1]
    # print(dp)
print(dp[-1])