# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# nums = list(map(int, input().split()))

# nums.sort()

# visited =[0] * n
# def permutations(arr):
#     global m
#     if len(arr) == m:
#         print(*arr)
#         return 
#     tmp = 0
#     for i in range(len(nums)):
#         if not visited[i] and tmp!=nums[i]:
#             visited[i] = 1
#             tmp= nums[i]
#             permutations(arr+[nums[i]])
#             visited[i] = 0
        
# permutations([])

# import sys
# input = sys.stdin.readline

# n, S =map(int, input().split())
# nums = list(map(int, input().split()))
# cnt, s, l = 0,0,0

# def dfs(start):
#     global s, cnt, l
#     if s == S and l>0:
#         cnt+=1
    
#     for i in range(start, n):
#         l+=1
#         s+=nums[i]
#         dfs(i+1)
#         l-=1
#         s-=nums[i]
        
# dfs(0)
# print(cnt)

# import sys
# from bisect import bisect_left
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = list(input().split() for _ in range(n))
    
# name, level = [i[0] for i in arr], [int(i[1]) for i in arr]

# for _ in range(m):
#     print(name[bisect_left(level, int(input()))])

# import sys
# input = sys.stdin.readline

# s = list(input().rstrip())
# q = int(input())

# cnt = {0: [0] * 26} # 길이가 key일 때, 알파벳 횟수 
 
# for i, ch in enumerate(s):
#     cnt[i+1] = cnt[len(cnt)-1][:]
#     cnt[i+1][ord(ch)-97]+=1

# for _ in range(q):
#     a, l, r = input().split()
#     print(cnt[int(r)+1][ord(a)-97]-cnt[int(l)][ord(a)-97])

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
    
print(dp)

ans = dp[0] # 0의 개수, i=j이고 m의 배수인 경우

for i in dp:
    if i>=2:
        ans += (i*(i-1))//2 # 조합

print(ans)
