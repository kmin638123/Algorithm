import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

prefix_sum = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, m+1):
        prefix_sum[i][j] = array[i-1][j-1]+prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(prefix_sum[x][y]-prefix_sum[x][j-1]-prefix_sum[i-1][y]+prefix_sum[i-1][j-1])
    