import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = input().rstrip()

stk = []

for i in range(n):
    while stk and stk[-1]<num[i] and k>0:
        stk.pop()
        k-=1
        
    stk.append(num[i])
    
if k>0:
    stk = stk[:-k]

print("".join(stk))