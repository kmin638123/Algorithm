import sys
from collections import deque
input = sys.stdin.readline

topni = [list(input().rstrip()) for _ in range(4)]
k = int(input())

for _ in range(k):
    idx, d = map(int, input().split())
    idx-=1
    left_idx, right_idx = idx-1, idx+1
    
    left_d = d
    l =[] #  l=r=[] 이렇게 했더니 l,r이 동기화되는 문제가 있었음...허걱...
    while 0<=left_idx:
        if topni[left_idx][2] != topni[left_idx+1][6]: # 왼쪽꺼 회전
            # print("left_rotate!: "+ str(left_idx))
            left_d *= -1
            l.append((left_idx, left_d))
            left_idx-=1
        else:
            break
    right_d = d
    r = []
    while right_idx<4:
        if topni[right_idx][6] != topni[right_idx-1][2]:
            # print("right_rotate!: "+ str(right_idx))
            right_d *= -1
            l.append((right_idx, right_d))
            right_idx+=1
        else:
            break
        
    for li, ld in l:
        left = deque(topni[li])
        left.rotate(ld)
        topni[li] = list(left)
        
    for ri, rd in r:
        right = deque(topni[ri])
        right.rotate(rd)
        topni[ri] = list(right)
    tmp = deque(topni[idx])
    tmp.rotate(d)
    topni[idx]=list(tmp)
    # print(topni)
    
    
ans = 0
for idx, t in enumerate(topni):
    ans+=int(t[0]) * (2**idx)
    

print(ans)