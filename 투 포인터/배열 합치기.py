import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []

i = j = 0
while i<n and j<m:
    if a[i] < b[j]:
        ans.append(a[i])
        i+=1
    else:
        ans.append(b[j])
        j+=1

if i<n:
    ans.extend(a[i:])
if j<m:
    ans.extend(b[j:])
    
print(*ans)
