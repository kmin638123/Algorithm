import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
answer = 0
while start <= end:
    mid = (start+end)//2
    cut = 0
    for t in trees:
        if t>mid:
            cut+=(t-mid)
    if m>cut:
        end = mid-1
    else: 
        answer = mid
        start = mid+1

print(answer)