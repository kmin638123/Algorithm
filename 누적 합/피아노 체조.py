import sys
input = sys.stdin.readline

n = int(input())
level = list(map(int, input().split()))

dp = [0]

for i in range(1,n):
    if level[i]<level[i-1]:
        dp.append(dp[i-1]+1)
    else:
        dp.append(dp[i-1])

# print(dp)

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(dp[y-1]-dp[x-1])