import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]

dp[0][nums[0]] = 1 # nums 첫번째 수 기록

for i in range(1,n-1): # n-1 숫자까지
    for j in range(21):
        if dp[i-1][j]: # 전까지 계산 결과가 존재하는 경우에만
            # 덧셈
            if j+nums[i]<=20:
                dp[i][j+nums[i]] += dp[i-1][j]
                
            # 뺄셈
            if j-nums[i] >=0:
                dp[i][j-nums[i]] += dp[i-1][j]
            
# print(dp)    
print(dp[n-2][nums[-1]])