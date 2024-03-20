import heapq
import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
s.sort(key= lambda x:(x[0],x[1]))

room = []
heapq.heappush(room, s[0][1])

for i in range(1, len(s)):
    if room[0]<=s[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, s[i][1])

print(len(room))
    
