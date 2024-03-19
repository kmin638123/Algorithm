from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().rstrip() for _ in range(n)]

ans = set()

for comb in permutations(cards, k):
    ans.add(int(''.join(comb)))
    
print(len(ans))