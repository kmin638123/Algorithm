import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]

start, end = 1, max(t) * m
answer = 0 
while start<=end:
    mid = (start+end)//2
    cnt = 0
    for time in t:
        cnt+= (mid//time)
    if cnt<m:
        start = mid+1
    else:
        answer= mid
        end = mid-1
print(answer)