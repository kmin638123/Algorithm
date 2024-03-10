# 나머지 합
# 시간 초과 풀이
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# dp = [0] + list(map(int, input().split()))

# for i in range(1, n+1):
#     dp[i] += dp[i-1]
    
# ans = 0 
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         # print(dp[i]-dp[j-1])
#         if (dp[i]-dp[j-1])%m == 0:
#             ans+=1
# print(ans)
#############################################

# (dp[j]-dp[i-1]) % m == 0 이 되는 부분 구간을 구하면 된다.
# 모듈러 연산의 경우 분배 법칙이 적용 가능!
# dp[j] % m == dp[i-1] % m 인 것, dp(누적합 배열)에서 나머지가 같은 두 인덱스를 고르면 된다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * m
dp[nums[0]%m]+=1

for i in range(1,n):
    nums[i] +=  nums[i-1]
    dp[nums[i]%m]+=1

ans = dp[0] # 0의 개수, i=j이고 m의 배수인 경우

for i in dp:
    if i>=2:
        ans += (i*(i-1))//2 # 조합

print(ans)
