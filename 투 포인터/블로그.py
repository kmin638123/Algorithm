# 시간 초과 풀이
# import sys
# input = sys.stdin.readline

# x, n = map(int, input().split())
# visit = list(map(int, input().split()))

# i, j = 0, n

# ans = cnt = 0

# while j <= len(visit):
#     day = sum(visit[i:j])
#     if ans == day:
#         cnt+=1
#     elif ans < day:
#         ans = day
#         cnt = 1
#     else:
#         pass
#     i+=1
#     j+=1

# if ans == 0:
#     print("SAD")
# else:
#     print(ans)
#     print(cnt)
            
#################################################
# 누적합을 사용해야 할 듯. 매번 sum을 해서 시간초과가 뜨는 것 같음
import sys
input = sys.stdin.readline

x, n = map(int, input().split())
visit = list(map(int, input().split()))

prefix_sum = [0] * (len(visit)+1)

for i in range(len(visit)):
    prefix_sum[i+1] = prefix_sum[i]+visit[i]

i, j = 0, n

ans = cnt = 0

while j <= len(visit):
    day = prefix_sum[j]-prefix_sum[i]
    if ans == day:
        cnt+=1
    elif ans < day:
        ans = day
        cnt = 1
    else:
        pass
    i+=1
    j+=1

if ans == 0:
    print("SAD")
else:
    print(ans)
    print(cnt)
