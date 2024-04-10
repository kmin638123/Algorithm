import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    files = []
    for f in arr:
        heapq.heappush(files, f)
    ans = 0 
    while len(files)>1:
        # 가장 작은 두개
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        ans+=(a+b)
        
        heapq.heappush(files, a+b)
        
    print(ans)