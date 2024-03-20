# 시간 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# time = [list(map(int, input().split())) for _ in range(n)]

# time.sort()

# room = [time[0][1]]

# for i in range(1,n):
#     t = time[i]
#     check = 0
#     for j in range(len(room)):
#         if room[j] <= t[0]:
#             room[j] = t[1]
#             check = 1
#             break
#     if not check:
#         room.append(t[1])
# print(len(room))
######################################
import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort()

room = []
heapq.heappush(room, time[0][1])

for i in range(1,n):
    t = time[i]
    if room[0] <= time[i][0]: # 제일 빨리 끝나는 타임
        heapq.heappop(room)
    heapq.heappush(room, time[i][1])

print(len(room))