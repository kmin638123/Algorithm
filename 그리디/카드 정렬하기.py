import sys
import heapq
input = sys.stdin.readline

n = int(input())

cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))
ans = 0 
while len(cards)>1:
    a = 0
    for _ in range(2):
        a+=heapq.heappop(cards)
    ans+=a
    heapq.heappush(cards, a)    
print(ans)       
