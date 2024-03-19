from itertools import combinations
import sys
input = sys.stdin.readline


n = int(input())
foods = [list(map(int, input().split())) for _ in range(n)]

ans = 1e9

for i in range(1, n+1):
    for comb in combinations(range(n), i):
        # print(comb)
        bitter = foods[comb[0]][1]
        sour = foods[comb[0]][0]
        for food in range(1,i):
            bitter += foods[comb[food]][1]
            sour *= foods[comb[food]][0]
        # print(sour, bitter)
        ans = min(ans, abs(bitter-sour))
        
print(ans)