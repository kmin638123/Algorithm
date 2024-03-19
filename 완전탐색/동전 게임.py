import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
                
def change(x):
    return 1 if x=="H" else 0

def check():
    row = set()
    for i in coins:
        j = set(i)
        if len(j)!=1:
            return False
        row.add(j.pop())
    return True if len(row)==1 else False

def column(idx):
    for i in range(3):
        coins[i][idx] = 1 - coins[i][idx]

def row(idx):
    for i in range(3):
        coins[idx][i] = 1 - coins[idx][i]
        
def diagonal(idx):
    if idx == 1:
        for i in range(3):
            coins[i][i] = 1- coins[i][i]
    else:
        for i in range(3):
            coins[i][2-i] = 1- coins[i][2-i]

def map_to_int(): # 2진수로 표현
    tmp = 0 
    for i in range(3):
        for j in range(3):
            tmp = tmp * 2 + coins[i][j]
    return tmp

def int_to_map(num):
    for i in range(3):
        for j in range(3):
            coins[2-i][2-j] = num % 2
            num = num // 2

for _ in range(t):
    coins = []
    for _  in range(3):
        coins.append(list(map(change, input().split())))
    
    cnt = 0
    ans = 1e9
    visited = [False] * 512 # 000 000 000 ~ 111 111 111
    
    queue = deque()
    current = map_to_int()
    queue.append((current, cnt))
    visited[current] = True
    
    p = 0
    
    while queue:
        current, cnt = queue.popleft()
        int_to_map(current)
        
        if check():
            print(cnt)
            p = 1
            break
        
        for i in range(3):
            row(i)
            next = map_to_int()
            if not visited[next]:
                visited[next] = True
                queue.append((next, cnt+1))
                
            # 다시 돌려놓기
            row(i)
                
        for i in range(3):
            column(i)
            next = map_to_int()
            if not visited[next]:
                visited[next] = True
                queue.append((next, cnt+1))
                
            # 다시 돌려놓기
            column(i)
                
        for i in range(2):
            diagonal(i)
            next = map_to_int()
            if not visited[next]:
                visited[next] = True
                queue.append((next, cnt+1))
                
            # 다시 돌려놓기
            diagonal(i)
            
    if not p:
        print(-1)    