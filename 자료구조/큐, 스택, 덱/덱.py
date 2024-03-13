from collections import deque
import sys
input = sys.stdin.readline
queue = deque()
n = int(input())
for _ in range(n):
    i = list(input().split())
    if len(i)>1:
        if i[0] == "push_back":
            queue.append(i[1])
        else:
            queue.appendleft(i[1])
        continue
    i = i[0]
    if i == "size": print(len(queue))
    elif i == "empty": print(1) if len(queue)==0 else print(0)
    else:
        if len(queue)==0:
            print(-1)
        else:
            num = 0
            if i=="pop_front":
                num = queue.popleft()
            elif i =="pop_back":
                num = queue.pop()
            elif i =="front":
                num = queue[0]
            else:
                num = queue[-1]
            print(num)