import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))

stk = []
ans = [0] * n

for i in range(n):
    # now = tower[i]
    # h = stk[-1]
    # if tower[h-1] > now:
    #     ans[i] = h
    #     stk.append(i+1)
    # else:
    #     h = stk.pop()
    #     while stk:
    #         h = stk.pop()
    #         if tower[h-1]>now:
    #             ans[i]=h
    #             break
    while stk:
        h = tower[stk[-1]]
        if h>tower[i]: # 부딪힘
            ans[i] = stk[-1] + 1
            break
        else: # 안부딪힘
            stk.pop()            
    
    stk.append(i) 

          
print(*ans)