# 징검다리 건너기 (small)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1

for i in range(n-1):
    if dp[i]==0:
        continue
    for j in range(i+1,n):
        if (j-i) * (1+abs(a[j]-a[i])) <= k:
            dp[j] = 1
            
ans = "YES" if dp[n-1] else "NO"
print(ans)

######################################
# 징검다리 건너기 
n = int(input())
energy = []
m = 1e9
for _ in range(n-1):
    e = list(map(int, input().split()))
    energy.append(e)

k = int(input())

if n == 1:
    print(0)
    exit()
if n == 2:
    print(energy[0][0])
    exit()

dp = [[m, m] for _ in range(n)]
dp[0][0] = 0
dp[1][0] = energy[0][0]
dp[2][0] = min(energy[0][0]+energy[1][0], energy[0][1])

for i in range(3, n):
    dp[i][0] = min(dp[i-2][0]+energy[i-2][1], dp[i-1][0]+energy[i-1][0])
    dp[i][1] = min(dp[i-3][0]+k, dp[i-2][1]+energy[i-2][1], dp[i-1][1]+energy[i-1][0])

print(min(dp[n-1][0], dp[n-1][1]))