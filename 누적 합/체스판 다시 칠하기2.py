
#############################################
# 체스판 다시 칠하기 2
# 시간 초과
# import sys

# input = sys.stdin.readline
# n, m, k = map(int, input().split())


# board = [list(input()) for _ in range(n)]

# def check(color):
#     prefix_sum = [[0] * (m+1) for _ in range(n+1)]
    
#     for i in range(n):
#         for j in range(m):
#             value = 0
#             if (i+j)%2==0:
#                 if color != board[i][j]:
#                     value = 1
#             else:
#                 if color == board[i][j]:
#                     value = 1
#             prefix_sum[i+1][j+1] = prefix_sum[i][j+1]+prefix_sum[i+1][j]-prefix_sum[i][j] + value
    
#     ans = n*m
    
#     for i in range(1, n-k+2):
#         for j in range(1, m-k+2):
#             ans = min(ans, prefix_sum[i+k-1][j+k-1]-prefix_sum[i-1][j+k-1]-prefix_sum[i+k-1][j-1]+prefix_sum[i-1][j-1])
#     return ans

# print(min(check("B"), check("W")))
#########################################################
# Python 3로 하면 시간 초과,,, PyPy3로 제출,,, 
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())


board = [list(input()) for _ in range(n)]

def check():
    prefix_sum_w = [[0] * (m+1) for _ in range(n+1)]
    prefix_sum_b = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            value_w = 0
            value_b = 0
            if (i+j)%2==0:
                if "W" != board[i][j]:
                    value_w = 1
                if "B"!= board[i][j]:
                    value_b = 1
            else:
                if "W" == board[i][j]:
                    value_w = 1
                if "B" == board[i][j]:
                    value_b = 1
            prefix_sum_w[i+1][j+1] = prefix_sum_w[i][j+1]+prefix_sum_w[i+1][j]-prefix_sum_w[i][j] + value_w
            prefix_sum_b[i+1][j+1] = prefix_sum_b[i][j+1]+prefix_sum_b[i+1][j]-prefix_sum_b[i][j] + value_b
            
    
    ans1 = n*m
    ans2 = n*m
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            ans1 = min(ans1, prefix_sum_w[i+k-1][j+k-1]-prefix_sum_w[i-1][j+k-1]-prefix_sum_w[i+k-1][j-1]+prefix_sum_w[i-1][j-1])
            ans2 = min(ans2, prefix_sum_b[i+k-1][j+k-1]-prefix_sum_b[i-1][j+k-1]-prefix_sum_b[i+k-1][j-1]+prefix_sum_b[i-1][j-1])

    return min(ans1, ans2)

print(check())
