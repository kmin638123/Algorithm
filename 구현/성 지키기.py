import sys
input = sys.stdin.readline

n, m = map(int, input().split())
castle = [list(input().rstrip()) for _ in range(n)]

row, col = 0,0

for i in range(n):
    line = castle[i]
    check = 0
    for j in line:
        if j=="X":
            check = 1
            break
        
    if not check:
        row += 1

for i in range(m):
    check = 0
    for j in range(n):
        if castle[j][i]=="X":
            check =1
            break
    if not check:
        col += 1

print(max(row, col))