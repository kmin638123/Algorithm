import sys
from itertools import combinations

s = sys.stdin.readline().rstrip()

stk = []
pair = []

for idx, i in enumerate(s):
    if i=='(':
        stk.append(idx)
    elif i== ")":
        left = stk.pop()
        pair.append((left, idx))
        
pair.sort()

ans = set()
for i in range(len(pair)):
    for comb in combinations(pair,i+1):
        tmp = list(s)
        for left, right in comb:
            tmp[left] = ""
            tmp[right] = ""
        
        ans.add("".join(tmp))

for i in sorted(list(ans)):
    print(i)