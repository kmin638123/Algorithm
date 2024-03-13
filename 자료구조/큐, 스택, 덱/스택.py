import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    i = list(input().split())
    if len(i) == 2:
        stack.append(i[1])
        continue
    i = i[0]
    if i=="top":
        print(stack[-1]) if len(stack)>0 else print(-1)
    elif i == "pop":
        if len(stack)==0:
            print(-1)
        else: 
            num=stack.pop()
            print(num)
    elif i == "size":
        print(len(stack))
    else:
        print(0) if len(stack)>0 else print(1)