# import sys
# from collections import Counter
# input = sys.stdin.readline

# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# i = 0
# j = 1

# ans = 0

# while j <= len(a):
#     l = a[i:j]
#     cnt = Counter(l).most_common(1)
#     m = cnt[0][1]
#     if m>k:
#         ans = max(ans, len(l)-1)
#         i=j-1
#     else:
#         j+=1
        
# print(ans)
##############################################
# 시간 초과!
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# i = 0
# j = 1

# ans = 0
# num = [0] * (max(a)+1)

# while j <= len(a):
#     l = a[i:j]
#     num[a[j-1]] +=1
#     m = max(num)
    
#     if m>k:
#         ans = max(ans, len(l)-1)
#         num = [0] * (max(a)+1)
#         i=j-1
#     else:
#         j+=1
        
# print(ans)

#############################################
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

i = j = 0

ans = 0
num = [0] * (max(a)+1)

while j < len(a):
    if num[a[j]] < k:
        num[a[j]] += 1
        j+=1
    else:
        num[a[i]]-=1
        i+=1
    ans = max(ans, j-i)
        
print(ans)