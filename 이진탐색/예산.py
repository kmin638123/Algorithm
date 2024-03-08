import sys

n = int(input())
request = list(map(int, sys.stdin.readline().split()))
total = int(input())
start, end = 0, max(request)

while start<=end:
    mid = (start+end)//2
    t = 0
    for r in request:
        if r>mid:
            t+=mid
        else:
            t+=r
            
    if t<=total:
        start = mid+1
    else:
        end = mid-1

print(end)
    
