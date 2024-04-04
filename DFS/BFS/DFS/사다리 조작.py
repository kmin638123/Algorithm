import sys
from itertools import combinations # 어김없이 시간초과!ㅎㅎ
input = sys.stdin.readline

n, m, h = map(int, input().split())

if m == 0: 
    print(0)
    exit()
    
sadari = [[False] * (n+1) for _ in range(h+1)]

for _ in range(m):
    a, b = map(int, input().split())
    sadari[a][b] = True

def check():
    # print(sadari)
    for i in range(1, n+1): # 세로선 하나하나 확인
        line = i # 현재 있는 세로선 위치!
        for j in range(1, h+1): # 밑으로 하나씩 내려가면서 확인
            if sadari[j][line]: # 오른쪽으로 이동
                line += 1
            elif sadari[j][line-1]: # 왼쪽으로 이동
                line -= 1
        if line != i:
            return False
    # print("Hi")
    return True
ans = 4

def dfs(cnt, x, y):
    global ans
    if check():
        if cnt == 0 or cnt==1: 
            print(cnt)
            exit()
        ans = min(cnt, ans)
    if cnt==3 or ans<=cnt:
        return
        
    for i in range(x, h+1):
        if i == x: # 행이 바뀌기 전에
            now = y
        else:
            now = 1
            
        for j in range(now, n):
             if not sadari[i][j] and not sadari[i][j+1]:
                 sadari[i][j] = True
                 dfs(cnt+1, i, j+2) # 연속으로 설치하면 안되기 때문 j+2
                 sadari[i][j] = False

dfs(0, 1, 1)

# cnt만 인자로 넘기면 시간초과!
# def dfs(cnt):
#     global ans
#     if check():
#         if cnt == 0 or cnt==1: 
#             print(cnt)
#             exit()
#         ans = min(cnt, ans)
#     if cnt==3 or ans<=cnt:
#         return
        
#     for i in range(1, h+1):
#         for j in range(1, n):
#              if not sadari[i][j]:
#                  sadari[i][j] = True
#                  dfs(cnt+1)
#                  sadari[i][j] = False

# dfs(0)

if ans < 4:
    print(ans)
else:   
    print(-1)
        