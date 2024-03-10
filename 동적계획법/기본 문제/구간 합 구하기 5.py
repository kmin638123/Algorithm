# 시간 초과 풀이
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# table = [list(map(int, input().split())) for _ in range(n)]

# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     dp = [[0] * n for _ in range(n)]
#     for i in range(x1-1,x2):
#         for j in range(y1-1,y2):
#             if j!=y2-1:
#                 dp[i][j] += (dp[i][j-1]+table[i][j])
#             else:
#                 dp[i][j] += (dp[i][j-1]+dp[i-1][j]+table[i][j])
#     # print(dp)
#     print(dp[x2-1][y2-1])
#############################################
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n+1)]
# dp에 누적합 저장하기
for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                dp[i+1][j+1] = table[i][j]
            else:
                dp[i+1][j+1] = table[i][j] + dp[i+1][j]
        elif j == 0:
            dp[i+1][j+1] = table[i][j]+dp[i][j+1]
        else:
            dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]-dp[i][j]+table[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])
    
    
