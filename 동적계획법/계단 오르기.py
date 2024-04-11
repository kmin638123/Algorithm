import sys
input = sys.stdin.readline

n = int(input())
steps =[int(input()) for _ in range(n)]

if n <=2:
    print(sum(steps))
    exit()
    
dp = [0] * (n)
dp[0] = steps[0]
dp[1] = steps[0]+steps[1]

for i in range(2,n):
    dp[i] = max(dp[i-3]+steps[i-1], dp[i-2])+steps[i]

# print(dp)
print(dp[-1])

