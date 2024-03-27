from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline

# for _ in range(10):
n= int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

queue =deque()
res = []

def move(board, d):
    for i in range(n-1):
        for j in range(n):
            if d == 3: # 오른쪽으로 이동
                idx = n-i-2
                if board[j][idx]!=0: # 0이 아니라면, 해당 방향에 0이 있으면 이동
                    while idx+1<n and board[j][idx+1]==0:
                        idx+=1
                    if idx == n-i-2: continue
                    board[j][idx]=board[j][n-i-2]
                    board[j][n-i-2] = 0
            elif d == 2: # 왼쪽으로 이동
                idx = i+1
                if board[j][idx]!=0:
                    while 0<=idx-1 and board[j][idx-1]==0:
                        idx-=1
                    if idx == i+1:
                        continue
                    board[j][idx] = board[j][i+1]
                    board[j][i+1] = 0
                
            elif d == 1: # 위쪽으로 이동
                idx = i+1
                if board[idx][j]!=0:
                    while 0<=idx-1 and board[idx-1][j]==0:
                        idx-=1
                    if idx == i+1: continue
                    board[idx][j] = board[i+1][j]
                    board[i+1][j]= 0
            else: # 아래로 이동
                idx = n-i-2
                if board[idx][j]!=0: # 0이 아니라면, 해당 방향에 0이 있으면 이동
                    while idx+1<n and board[idx+1][j]==0:
                        idx+=1
                    if idx == n-i-2: continue
                    board[idx][j]=board[n-i-2][j]
                    board[n-i-2][j] = 0
    return board
                    
def plus(board, d):
    visited = [[False]*n for _ in range(n)]
    for i in range(n-1): # 한 칸 씩 d 방향으로 n-1번 이동!!
        for j in range(n): # n 줄 모두 이동
            if d == 3: # 오른쪽으로 이동
                idx = n-i-2
                if board[j][idx]!=0: # 0이 아니라면, 해당 방향에 0이 있으면 이동
                    while idx+1<n and board[j][idx+1]==0:
                        idx+=1
                    if idx+1<n and board[j][idx+1]==board[j][n-i-2] and not visited[j][idx+1]: 
                        board[j][idx+1] *= 2
                        visited[j][idx+1] = True
                        board[j][n-2-i] = 0
                
            elif d == 2: # 왼쪽으로 이동
                idx = i+1
                if board[j][idx]!=0:
                    while 0<=idx-1 and board[j][idx-1]==0:
                        idx-=1
                    if 0<=idx-1 and board[j][idx-1]==board[j][i+1] and not visited[j][idx-1]:
                        visited[j][idx-1] = True
                        board[j][idx-1]*= 2
                        board[j][i+1]= 0
                    
            elif d == 1: # 위쪽으로 이동
                idx = i+1
                if board[idx][j]!=0:
                    while 0<=idx-1 and board[idx-1][j]==0:
                        idx-=1
                    if 0<=idx-1 and board[idx-1][j] == board[i+1][j] and not visited[idx-1][j]:
                        board[idx-1][j] *= 2
                        visited[idx-1][j] = True
                        board[i+1][j] = 0
            else: # 아래로 이동
                idx = n-i-2
                if board[idx][j]!=0: # 0이 아니라면, 해당 방향에 0이 있으면 이동
                    while idx+1<n and board[idx+1][j]==0:
                        idx+=1
                    if idx+1<n and board[idx+1][j] == board[n-i-2][j] and not visited[idx+1][j]:
                        board[idx+1][j] *= 2
                        visited[idx+1][j] = True
                        board[n-2-i][j] = 0
    return move(board, d)

# print(plus(board, 1))
queue.append((board, 0))
while queue:
    b, cnt = queue.popleft()
    if cnt == 5:
        tmp = 0
        for i in range(n):
            tmp = max(tmp, max(b[i]))
        res.append(tmp)
        continue
    
    for i in range(4):
        copy_board = deepcopy(b)
        queue.append((plus(copy_board,i), cnt+1))
        
print(max(res))