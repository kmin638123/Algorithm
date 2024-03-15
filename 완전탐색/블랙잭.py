import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

mm = m
ans = 0

for i in combinations(cards,3):
    s = sum(i)
    if 0<=m-s<mm:
        ans = s
        mm = m-s
    
print(ans)