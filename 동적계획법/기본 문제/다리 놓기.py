# 시간 초과
# import sys
# from itertools import combinations

# input = sys.stdin.readline
# t =int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     print(len(list(combinations(list(range(m)),n))))

########################################
# dp 
import sys
input = sys.stdin.readline
t= int(input())

dp = [[0]* 31 for _ in range(31)]

for i in range(1,31):
    for j in range(1,31):
        if i == 1:
            dp[i][j]=j
        else:
            if i==j:
                dp[i][j]=1
            elif i<j:
                dp[i][j]= dp[i][j-1]+dp[i-1][j-1]
                
for _ in range(t):
    n ,m = map(int, input().split())
    print(dp[n][m])