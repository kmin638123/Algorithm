# # 가장 긴 증가하는 부분 수열
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = list(map(int, input().split()))

# d = [1] * (n) # DP 테이블 초기화

# for i in range(1,n):
#     for j in range(0,i):
#         if array[j] < array[i]:
#             d[i] = max(d[i],d[j]+1)

# print(max(d)) 

# ############################################
# # 가장 긴 바이토닉 부분 수열
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = list(map(int, input().split()))

# dp1 = [1] * (n) # DP 테이블 초기화
# dp2 = [1] * (n) # DP 테이블 초기화

# for i in range(1,n):
#     for j in range(0,i):
#         if array[j] < array[i]:
#             dp1[i] = max(dp1[i],dp1[j]+1)

# array.reverse()
# for i in range(1,n):
#     for j in range(0,i):
#         if array[j] < array[i]:
#             dp2[i] = max(dp2[i],dp2[j]+1)
            
# dp2.reverse()

# dp = [0] * n
# for i in range(n):
#     dp[i] = dp1[i]+dp2[i]

# print(max(dp)-1) 
# ############################################
# # 가장 큰 증가하는 부분 수열
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = list(map(int, input().split()))

# dp = [0] * (n) # DP 테이블 초기화
# dp[0] = array[0]
# for i in range(1,n):
#     for j in range(i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i],dp[j]+array[i])
            
#         else:
#             dp[i] = max(array[i], dp[i])

# print(max(dp)) 
# ############################################
# # 가장 긴 감소하는 부분 수열
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = list(map(int, input().split()))

# dp = [1] * (n) # DP 테이블 초기화
# array.reverse()
# for i in range(1,n):
#     for j in range(i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i],dp[j]+1)
            

# print(max(dp)) 

# ############################################
# # 가장 긴 증가하는 부분 수열 4 
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = list(map(int, input().split()))

# dp = [1] * (n) # DP 테이블 초기화
# trace = [i for i in range(n)] 

# for i in range(1,n):
#     for j in range(i):
#         if array[j] < array[i]:
#             # dp[i] = max(dp[i],dp[j]+1)
#             if dp[i]<dp[j]+1:
#                 dp[i] = dp[j]+1
#                 trace[i] = j
                
# ans = max(dp)
# idx = dp.index(ans)
# nums = []

# while True:
#     nums.append(array[idx])
#     if idx == trace[idx]:
#         break
#     idx = trace[idx]
    
# print(ans) 
# print(*reversed(nums))

############################################
# 가장 긴 짝수 연속한 부분 수열 
# 다시 풀기
n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    s[i] %= 2
    for j in range(k+1):
        if s[i] == 0: #짝수일 때
            dp[i][j] = dp[i-1][j] + 1
        if j != 0 and s[i]: #홀수일 때 
            dp[i][j] = dp[i-1][j-1]
            
result = []
for i in dp:
    result.append(i[k])
# print(dp)
print(max(result))