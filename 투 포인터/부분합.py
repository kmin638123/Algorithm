# 시간 초과 풀이ㅠ
# import sys
# input = sys.stdin.readline

# n, s= map(int, input().split())
# arr = list(map(int, input().split()))

# prefix_sum = [0] * (n+1)

# for i in range(n):
#     prefix_sum[i+1] = prefix_sum[i]+arr[i]

# ans = 100001

# for i in range(n-1):
#     for j in range(i+1,n):
#         tmp = prefix_sum[j]-prefix_sum[i]
#         if tmp>=s:
#             ans = min(ans, j-i)
#             break
        

# ans = ans if ans!=100001 else 0
# print(ans)
#############################################
# 일단 논리를 잘 짜는 게 중요하구만

import sys
input = sys.stdin.readline

n, s= map(int, input().split())
arr = list(map(int, input().split()))

i = j = 0
sum = 0
ans = 100001
# while j<n:
#     if sum < s:
#         sum+=arr[j]
#         j+=1
#     else:
#         ans = min(ans, j-i)
#         sum-=arr[i]
#         i+=1
while True:
    if sum >= s:
        ans = min(ans, j-i)
        sum -= arr[i]
        i+=1
    else:
        if j==n:
            break
        sum+=arr[j]
        j+=1

ans = ans if ans!=100001 else 0
print(ans)