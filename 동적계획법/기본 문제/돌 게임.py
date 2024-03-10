# dp 
n = int(input())

dp = [-1] * 1000 # dp 테이블 초기화
dp[0] = 0 # 0은 SK
dp[1] = 1 # 1은 CY
dp[2] = 0

for i in range(3,n):
    if dp[i-1]==0 or dp[i-3]==0:
        dp[i]=1
    else:
        dp[i]=0
        
ans = "SK" if dp[n-1]==0 else "CY"
print(ans)

##################################
# 간단한 방법
# 홀수면 SK, 짝수면 CY
n = int(input())
ans = "SK" if n%2==1 else "CY"
print(ans)