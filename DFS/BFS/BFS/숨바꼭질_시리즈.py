# 숨바꼭질
from collections import deque
n, k = map(int, input().split())

dist = [0] * 100001

queue = deque()

queue.append(n)

while queue:
    num = queue.popleft()
    if num==k:
        print(dist[num])
        break
    
    for new in (num+1,num-1,num*2):
        if 0<=new<=100000 and dist[new]==0:
            dist[new]=dist[num]+1
            queue.append(new)
#######################################
# 숨바꼭질 2

from collections import deque
n, k = map(int, input().split())

dist = [0] * 100001

queue = deque()
queue.append(n)

time = 100001
tmp = 0
while queue:
    num = queue.popleft()
    if num==k:
        if dist[num]<time:
            tmp = 1
            time = dist[num]
        elif time == dist[num]:
            tmp+=1
    
    for new in (num+1,num-1,num*2):
        # 가능한 경로를 다 계산해줘야 하기 때문에
        # 들렸던 점을 또 갈 수 있다. 그렇기 때문에
        # dist[new]==0 만을 조건으로 달면, 갔던 곳을 또 가지 못해서 
        # 해당 경우는 계산하지 못한다. 따라서, 최소 경로를 따지기 위해
        # dist[new]==dist[num]+1를 조건에 추가해준다!
        if 0<=new<=100000 and (dist[new]==0 or dist[new]==dist[num]+1):
            dist[new]=dist[num]+1
            queue.append(new)      

print(time)
print(tmp)

##########################################
# 숨바꼭질 3
from collections import deque
n, k = map(int, input().split())

dist = [0] * 100001

queue = deque()

queue.append(n)

while queue:
    num = queue.popleft()
    if num==k:
        print(dist[num])
        break
    
    for new in (num*2, num-1,num+1):
        if 0<=new<=100000 and dist[new]==0:
            if new == num*2:
                dist[new]=dist[num]
            else:
                dist[new]=dist[num]+1
            queue.append(new)

##########################################
# 숨바꼭질 4 - 메모리 초과 풀이
from collections import deque
n, k = map(int, input().split())

dist = [[0, [i]] for i in range(100002)]

queue = deque()

queue.append(n)

while queue:
    num = queue.popleft()
    if num==k:
        print(dist[num][0])
        print(*reversed(dist[num][1]))
        break
    
    for new in (num*2,num-1,num+1):
        if 0<=new<=100000 and dist[new][0]==0:
            dist[new][0]=dist[num][0]+1
            dist[new][1]+=dist[num][1]
            queue.append(new)
            
# ##########################################
# 숨바꼭질 4 
from collections import deque
import sys
sys.setrecursionlimit(1000000000)

n, k = map(int, input().split())

dist = [0] * 100001
path = [0] * 100001 # 이전의 점을 기록하는 리스트

queue = deque()

queue.append(n)
path[n]=n

def print_path(dist,k):
    p = [k]
    for i in range(dist):
        p.append(path[k])
        k = path[k]
    print(*reversed(p))
    return

while queue:
    num = queue.popleft()
    if num==k:
        print(dist[num])
        print_path(dist[num],k)
        break
    
    for new in (num-1,num+1,num*2): # (num*2,num-1,num+1) 순으로 하면 틀림...(?) 왜?
        if 0<=new<=100000 and dist[new]==0:
            dist[new]=dist[num]+1
            path[new]=num
            queue.append(new)