import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

loop = min(n,m)//2 # 회전 개수
arr = [[0]*m for _ in range(n)]
queue = deque()

for i in range(loop):
    queue.clear()
    queue.extend(a[i][i:m-i]) # 위
    queue.extend([row[m-1-i] for row in a[i+1:n-1-i]]) # 오른쪽
    queue.extend(a[n-i-1][i:m-i][::-1]) # 아래를 왼쪽부터
    queue.extend([row[i] for row in a[i+1:n-i-1]][::-1]) # 왼쪽을 아래부터
    
    queue.rotate(-r)
    
    for j in range(i,m-i): # 위
        arr[i][j] = queue.popleft()
    for j in range(i+1, n-1-i): # 오른쪽
        arr[j][m-i-1] = queue.popleft()
    for j in range(m-i-1,i-1,-1):
        arr[n-i-1][j] = queue.popleft()
    for j in range(n-i-2, i, -1):
        arr[j][i] = queue.popleft()

for row in arr:
    print(*row, sep=" ")        
        