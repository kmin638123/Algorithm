#  시간 초과 풀이
# import sys
# x = sys.stdin.readline().rstrip()

# stk = []

# ans = 0

# for idx in range(len(x)):
#     i = x[idx]
#     # print("x: "+i)
#     if i == "(":
#         stk.append(0)
#     else:
#         if x[idx-1] == "(": # laser라는 뜻
#             stk.pop()
#             stk = list(map(lambda x:x+1, stk))
#             continue
            
#         stick = stk.pop()
#         if stick:
#             ans+=(stick+1)
#     # print("stick: ", end=" ")       
#     # print(stk)
            
# print(ans)
#################################

import sys
x = sys.stdin.readline().rstrip()

stk = []

ans = 0

for idx in range(len(x)):
    i = x[idx]
    # print("x: "+i)
    if i == "(":
        stk.append("(")
    else:
        if x[idx-1] == "(": # laser라는 뜻
            stk.pop()
            ans += len(stk)
        else:
            stk.pop()
            ans+=1 # 해당 막대기의 나머지 부분을 더해주는 거임
            
print(ans)