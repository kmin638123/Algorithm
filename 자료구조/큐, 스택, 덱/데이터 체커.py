# import sys
# input = sys.stdin.readline

# n = int(input())
# circle = [list(map(int, input().split())) for _ in range(n)] # x, r

# circle.sort(key = lambda x:(x[0]+x[1]))
# stk = []
# for x, r in circle:
#     while stk:
#         cx, cr = stk.pop()
#         if cx==x: 
#             if cr ==r: # 똑같은 원
#                 print("NO")
#                 exit()
#             break # 동심원은 pass!
#         else: # cx+cr < x-r 이어야 안 만남
#             if (cx+cr) < x-r: # 외부에서 안 만남
#                 continue
#             elif abs(x-cx)<abs(r-cr): # 포함
#                 continue
#             else:
#                 print("NO")
#                 exit()
#     stk.append((x,r))
            
# print("YES")
##################################################################
    
# 어떤 원의 왼쪽 끝 점과 오른쪽 끝 점 사이에 짝지어 지지 못한 
# 다른 원의 왼쪽 끝점이 존재한다면 원이 겹치는 거

import sys
input = sys.stdin.readline
n = int(input())
circle = []
for i in range(n):
    x, r = map(int, input().split())
    circle.append((x-r, i))
    circle.append((x+r, i))
    
circle.sort()

stk = []
for d, i in circle:
    if stk:
        if stk[-1]==i:
            stk.pop()
        else:
            stk.append(i)
    else:
        stk.append(i)
            
# print(stk)
if stk:
    print("NO")
else:
    print("YES")