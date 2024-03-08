import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]

start, end = 1, max(l)
answer = 0 

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in l:
        cnt += (i//mid)
    if cnt < m:
        end = mid-1
    else:
        answer = mid
        start = mid+1
    
print(answer)