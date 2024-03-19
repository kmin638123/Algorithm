from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
like = list(list(map(int, input().split())) for _ in range(n))

ans = 0

for comb in combinations(range(m), 3):
    tmp = 0
    for i in like:
        tmp+= max(i[comb[0]], i[comb[1]], i[comb[2]])
    ans = max(tmp, ans)
    
print(ans)