import sys
input = sys.stdin.readline
drinks = [0] * 10000
n = int(input())
for i in range(n):
    drinks[i]=int(input())
    
dp=[drinks[0]]
dp.append(drinks[0]+drinks[1])
dp.append(max(drinks[0]+drinks[2], drinks[1]+drinks[2],drinks[0]+drinks[1]))
for i in range(3,n):
    dp.append(max(dp[i-3]+drinks[i-1]+drinks[i],dp[i-1],dp[i-2]+drinks[i]))

print(dp[n-1])

##########################
# 2회차 풀이

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0] * n

if n == 1:
    print(arr[0])
    exit()

dp[0],dp[1] = arr[0], arr[0] + arr[1]

for i in range(2,n):
    # 마시지 않는 경우도 고려해 줘야 함
    dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1]) 
print(dp[n-1])
