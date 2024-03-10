#############################################
# 구간 합 구하기 4
# index로 리스트 자르고, sum 함수 쓰면 시간 초과!
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [0] + list(map(int, input().split()))

for i in range(1,n+1):
    dp[i]+=dp[i-1]

for _ in range(m):
    a, b= map(int, input().split())
    print(dp[b]-dp[a-1])
