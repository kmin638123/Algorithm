import sys
input = sys.stdin.readline


n, k = map(int, input().split())
stk = list(range(1,n+1))

idx = 0
ans = []

while len(stk)>0:
    
    # idx = (idx-1+k) % len(stk)
    idx += (k-1)
    if idx>= len(stk):
        idx %= len(stk)
        
    # num = stk[idx]
    # stk.remove(num)
    # ans.append(str(num))
    ans.append(str(stk.pop(idx)))    
    
print("<"+", ".join(ans)+">")