import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))

i, j = 0, 1
ans = 0 if s[i]%2==1 else 1
odd = 1 if s[i]%2==1 else 0

while j < n:
    # print(i, j, odd)
    if odd<=k:
        if s[j]%2==1:
            odd+=1
        j+=1
    else:    
        # print(i)
        if s[i]%2==1:
            odd-=1
        i+=1
    
    if odd<=k:
        ans = max(ans, j-i-odd)
        

print(ans)