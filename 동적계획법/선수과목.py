import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [1] * (n+1) # dp[i] = i번째 과목을 몇 학기에 이수할 수 있는 지

arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort()

for i in range(m):
    a, b= arr[i]
    dp[b] = max(dp[b],dp[a]+1)
    
print(*dp[1:])