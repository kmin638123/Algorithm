# 투 포인터(백준 22862)
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# s = list(map(int, input().split()))

# i,j, ans,cnt = 0,1,0,0

# if s[0]%2==1: #수열 첫번째 원소가 홀수일 때,
#     cnt = 1
# else:
#     ans = 1


# while j<n:
#     if cnt<=k:
#         if s[j]%2!=0: # 홀수
#             cnt+=1
#         j+=1
    
#     else:
#         if s[i]%2==1:
#             cnt-=1
#         i+=1
    
#     if cnt<=k:        
#         ans = max(ans, j-i-cnt)
#     # print(i,j)       
# print(ans)

###############################################################3
# dp

# # 백준 15486
# import sys
# input = sys.stdin.readline

# n = int(input())
# schedule = [list(map(int, input().split())) for _ in range(n)]

# dp = [0] * (n+1)

# for i in range(n):
#     dp[i+1] = max(dp[i],dp[i+1])
#     c = i+schedule[i][0]
#     if c<=n: # 퇴사일 전까지라면!
#         dp[c] = max(dp[c], dp[i]+schedule[i][1])

# print(dp[-1])

# # 백준 2156
# import sys
# input = sys.stdin.readline

# n = int(input())
# podo = list(int(input()) for _ in range(n))

# if n<=2:
#     print(sum(podo))
#     exit()

# dp = [0] * (n)
# dp[0] = podo[0]
# dp[1] = podo[0]+podo[1]
# dp[2] = max(dp[1],dp[0]+podo[2],podo[1]+podo[2])


# for i in range(3,n):
#     dp[i] = max(dp[i-3]+podo[i-1]+podo[i],dp[i-2]+podo[i],dp[i-1])
    
# print(dp[-1])

# # 백준 10844
# import sys
# n = int(sys.stdin.readline())

# dp = [[1] * 10 for _ in range(n)]

# dp[0][0] = 0

# for i in range(1,n):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i-1][j+1]
#         elif j==9:
#             dp[i][j] = dp[i-1][j-1]
#         else:
#             dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1])
            
# print(sum(dp[-1]) % 1000000000)

# # 백준 1106
# import sys
# input = sys.stdin.readline

# c, n = map(int, input().split())
# info = [list(map(int, input().split())) for _ in range(n)]
# info.sort(key = lambda x: (x[1],x[0]))

# dp = [0] + [1e9] * (c+info[-1][1])

# for i in range(1, len(dp)):
#     for j in range(n):
#         p = info[j]
#         if i-p[1]<=0:
#             dp[i] = min(dp[i], p[0])
#         else:
#             dp[i] = min(dp[i], dp[i-p[1]]+p[0])
            
# print(dp[c])

# # 백준 2293
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# coins = list(int(input()) for _ in range(n))
# coins.sort()

# dp = [0] * (k+1)

# for coin in coins:
#     for i in range(1, k+1):
#         if i-coin>0:
#             dp[i]+=dp[i-coin]
#         elif i==coin:
#             dp[i] += 1
            
# print(dp[-1])

# 백준 2294
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
coins.sort()

dp = [1e9] * (k+1)

for i in range(1, k+1):
    for coin in coins:
        if i<coin:
            pass
        elif i ==coin:
            dp[i] = 1
        else:
            dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[-1] if dp[-1]!=1e9 else -1)