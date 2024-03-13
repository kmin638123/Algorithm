from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

queue = deque()

for _ in range(n):
    i = list(input().split())
    if len(i) == 2:
        queue.append(i[1])
        continue
    i = i[0]
    if i == "pop":
        if len(queue)==0:
            print(-1)
        else:
            num = queue.popleft()
            print(num)
    elif i == "size":
        print(len(queue))
    elif i == "empty":
        print(1) if len(queue)==0 else print(0)
    else:
        if len(queue)==0:
            print(-1)
        else:
            if i == "front": print(queue[0])
            else: print(queue[-1])
    