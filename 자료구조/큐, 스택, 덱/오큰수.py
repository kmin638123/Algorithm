# n^2의 시간복잡도
# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))

# for i in range(n):
#     ai = a[i]
#     check = 0 
#     for j in range(i+1, n):
#         if a[j]>ai:
#             check = 1
#             print(a[j], end=" ")
#             break
#     if not check:
#         print(-1, end=" ")

#########################################
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = [-1] * n
stk = []
for i in range(n):
    while stk and stk[-1][0] < a[i]: 
        num, idx = stk.pop()
        ans[idx] = a[i]
    stk.append((a[i],i))
print(*ans) 