# 최대 힙
import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    x = int(input())
    if not x:
        if len(heap)==0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)

##############################################
# 최소 힙
import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    x = int(input())
    if not x:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)