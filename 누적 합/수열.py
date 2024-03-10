#############################################
# 수열
# 시간 초과 풀이
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# nums = list(map(int, input().split()))

# start, idx = 0, k
# ans = sum(nums[start:idx])
# idx+=1
# start+=1

# while idx <=n:
#     ans = max(ans, sum(nums[start:idx]))
#     idx+=1
#     start+=1
    
# print(ans)
######################################################
# 누적합 풀이
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# nums = list(map(int, input().split()))

dp = [0] + list(map(int, input().split()))

for i in range(1,n+1):
    dp[i]+=dp[i-1]

ans = dp[k]-dp[0]
for i in range(k+1, n+1):
    ans = max(ans, dp[i]-dp[i-k])
print(ans)
