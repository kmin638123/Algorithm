import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

ice = [[False] * n for _ in range(n)]

for i in range(m):
    a, b  = map(int,input().split())
    ice[a-1][b-1] = True
    ice[b-1][a-1] = True

ans = 0

for comb in combinations(range(n), 3):
    # print(comb)
    if ice[comb[0]][comb[1]] or ice[comb[1]][comb[2]] or ice[comb[0]][comb[2]]:
        continue
    ans+=1
print(ans)