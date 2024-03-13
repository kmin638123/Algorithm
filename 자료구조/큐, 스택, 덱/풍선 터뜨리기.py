from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
queue = deque()

for i in range(n):
    queue.append((i+1, b[i]))    

while queue:
    idx, move = queue.popleft()
    print(idx, end= " ")
    
    if move>0:
        move -= 1
    queue.rotate(-move)
            