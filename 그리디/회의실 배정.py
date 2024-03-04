import sys
n = int(input())

time = []
for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key= lambda x:(x[0],x[1]))

stack = []
stack.append(time[0])

for i in range(1,n):
    t = stack.pop()
    new = time[i]
    if new[0]>=t[1]:
        stack.append(t)
        stack.append(new)
        continue
    else:
        if new[1]<t[1]:
            stack.append(new)
        else:
            stack.append(t)
# print(stack)
print(len(stack))