from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
comb = list(permutations(range(1,10),3))

for _ in range(n):
    q, s, b = map(int, input().split())
    q = list(map(int, str(q)))
    cnt = 0
    for i in range(len(comb)):
        i-=cnt
        st, ball = 0,0
        for j in range(3):
            if comb[i][j] == q[j]:
                st+=1
            elif q[j] in comb[i]:
                ball+=1
        if st!=s or ball!=b:
            comb.remove(comb[i])
            cnt+=1
            
print(len(comb))