import sys
input = sys.stdin.readline

c, n = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

city.sort(key=lambda x:(x[1], x[0]))

dp = [0]+[1e9] * (c+city[-1][1])

for i in range(1,len(dp)):
    for j in range(len(city)):
        p = city[j]
        if i-p[1]<=0:
            dp[i] = min(dp[i], p[0])
        else:
            dp[i] = min(dp[i], dp[i-p[1]]+p[0])

print(min(dp[c:]))
