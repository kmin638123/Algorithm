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
