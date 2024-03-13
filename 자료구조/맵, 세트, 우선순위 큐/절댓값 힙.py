import sys
import heapq
input = sys.stdin.readline

n = int(input())
plus_heap = [] 
minus_heap = [] # 음수들을 max_heap으로 저장

for _ in range(n):
    x = int(input())
    if x==0:
        if len(plus_heap)+len(minus_heap)==0:
            print(0)
        elif not plus_heap: #  plus_heap만 비어있음
            print(-heapq.heappop(minus_heap))
        elif not minus_heap: 
            print(heapq.heappop(plus_heap))
        else:
            p = plus_heap[0]
            m = minus_heap[0]
            if abs(p)==abs(m):
                print(-heapq.heappop(minus_heap))
            elif abs(p)>abs(m):
                print(-heapq.heappop(minus_heap))
            else:
                print(heapq.heappop(plus_heap))
    else:
        if x>0:
            heapq.heappush(plus_heap, x)
        else:
            heapq.heappush(minus_heap, -x)
            