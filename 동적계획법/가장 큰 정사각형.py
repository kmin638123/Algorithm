import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]

# dp 준비
dp = [[0]*m for _ in range(n)]
dp[0] = board[0]
ans = max(board[0])

for i in range(1,n):
    dp[i][0] = board[i][0]
    ans = max(dp[i][0],ans)
    
for i in range(1, n):
    for j in range(1, m):
        if board[i][j]:
            board[i][j] = min(board[i-1][j], board[i][j-1],board[i-1][j-1])+1
            ans = max(ans, board[i][j])
            
print(ans**2)