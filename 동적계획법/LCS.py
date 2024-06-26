import sys
input = sys.stdin.readline

a = ' '+input().rstrip()
b = ' '+input().rstrip()

dp = [[0] * len(a) for _ in range(len(b))]

for i in range(1,len(b)):
    for j in range(1,len(a)):
        if b[i] == a[j]:
            dp[i][j] =  dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])