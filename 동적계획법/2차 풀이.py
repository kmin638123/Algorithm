# 퇴사 2 
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)

for i in range(n):
    dp[i+1] = max(dp[i+1], dp[i])
    tmp = arr[i]
    if i+tmp[0]<=n:
        dp[i+tmp[0]] = max(dp[i+tmp[0]], dp[i]+tmp[1])
        
print(dp[-1])
#############################################################33
# 호텔
import sys
input = sys.stdin.readline

c, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
city.sort(key= lambda x:x[1])

dp = [0]+[1e9] * (c+city[-1][1])

for i in range(1, len(dp)):
    for cost, people in city:
        if i <= people:
            dp[i] = min(dp[i], cost)
        else:
            dp[i] = min(dp[i-people]+cost, dp[i])
            
print(min(dp[c:]))

##########################################################
# 동전 1
import sys
input = sys.stdin.readline

n , k = map(int, input().split())
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
            dp[i] += dp[i-coin]
        
print(dp[-1])
##########################################################
# 동전 2
import sys
input = sys.stdin.readline

n , k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [1e9] * (k+1)

for coin in coins:
    for i in range(1, k+1):
        if i<coin:
            continue
        if i == coin:
            dp[i]=1
        else:
            dp[i] = min(dp[i-coin]+1,dp[i])

print(dp[-1] if dp[-1]!=1e9 else -1)

##########################################################
# 동전 
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m+1)
    for coin in coins:
        for i in range(1,m+1):
            if i<coin:
                continue
            if i==coin:
                dp[i] +=1
            else:
                dp[i] += dp[i-coin]
                
    print(dp[-1])

##########################################################
# 평범한 배낭 
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
obj = [[0,0]]+[list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k+1) for _ in range(n+1)] # dp[i][j]: 물품 i까지 담았을 때, j 무게 배낭의 최대 가치

for i in range(1,n+1):
    # i 번째
    w, v = obj[i]
    for j in range(1,k+1): # 무게
        if j>=w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
        
##########################################################
# LCS
import sys
input = sys.stdin.readline

a = " "+input().rstrip()
b = " "+input().rstrip()

dp = [[0] * (len(a)) for _ in range(len(b))]

for i in range(1,len(b)):
    for j in range(1,len(a)):
        if b[i]==a[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
print(dp[-1][-1])

        
##########################################################
# 합분해
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n+1)]

dp[0] =  [1] * (k+1)

for i in range(1,n+1):
    for j in range(1,k+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
print(dp[-1][-1] % 1000000000)

##########################################################
# 설탕 배달
import sys
input = sys.stdin.readline

n = int(input())

dp = [-1] * (n+1)

for i in range(3,n+1):
    if i==3 or i==5:
        dp[i] = 1
        continue
    if dp[i-5]>0:
        dp[i] = min(dp[i], dp[i-5]+1) if dp[i]!=-1 else dp[i-5]+1
    if dp[i-3]>0:
        dp[i] = min(dp[i], dp[i-3]+1) if dp[i]!=-1 else dp[i-3]+1
print(dp[-1])