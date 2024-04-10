# import sys
# input = sys.stdin.readline

# n = int(input())
# limit = list(map(int, input().split()))
# limit.sort(reverse=True)
# m = int(input())
# box = list(map(int, input().split()))
# box.sort(reverse=True)

# if box[0]> limit[0]:
#     print(-1)
#     exit()
    
# idx, time = 0, 0 
# moved = set()
# tmp = 0
# while len(moved)<m:
#     time+=1
#     for weight in limit:
#         if idx in moved:
#             while idx in moved:
#                 idx+=1
#         if idx==m: break
#         if idx not in moved and box[idx] <= weight:
#             moved.add(idx)
#             idx+=1
#             tmp=idx
#         else:
#             for i in range(tmp, m):
#                 if i not in moved and box[i]<=weight:
#                     moved.add(i)
#                     break
#                 tmp+=1
        
# print(time)

#######################################################################3
import sys
input = sys.stdin.readline

n = int(input())
limit = list(map(int, input().split()))
limit.sort(reverse=True)
m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

if box[0]> limit[0]:
    print(-1)
    exit()
    
time = 0
while box:
    time += 1
    for weight in limit:
        if not box:
            print(time)
            exit()
        if weight < box[-1]:
            continue
        for box_w in box:
            if box_w<=weight:
                box.remove(box_w)
                break
print(time)