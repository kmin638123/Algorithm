import sys
input = sys.stdin.readline

n = int(input())

now = 1
stk = []
ans = []

check = 0

for _ in range(n):
    num = int(input())

    while now<=num:
        stk.append(now)
        ans.append("+")
        now+=1
        # print("+")
        
    if stk[-1]==num:
        stk.pop()
        ans.append("-")
    else:
        print("NO")
        check = 1
        break
            
    # print(stk)
    
if not check:
    for a in ans:
        print(a)