import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    row = list(map(int, input().split()))
    if not heap:
        for r in row:
            heapq.heappush(heap, r)
    else: # 항상 heap을 n의 길이로 유지
        for r in row:
            if heap[0]<r:
                heapq.heappush(heap, r)
                heapq.heappop(heap)
                
print(heap[0]) # n 번째로 큰 수는 큰 수 n개 중 가장 작은 수!