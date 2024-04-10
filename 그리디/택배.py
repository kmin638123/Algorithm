import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

info = [list(map(int, input().split())) for _ in range(m)]
info.sort(key=lambda x:x[1]) # 도착지 기준으로 배열

capacity = [c] * (n+1) # 각 마을에서의 트럭 용량
ans = 0 

for s, r, box in info:
    deliever = box
    
    # s에서 box를 싣고 r로 쭉 이동하기 때문에, (s,r) 까지의 용량이 이를 담을 수 있어야 한다.
    # 만약, (s,r)까지의 용량 중에 box 보다 작은 것이 있다면, 최대로 옮길 수 있는 박스는 
    # min(capacity[i],deliever) 가 되는 것.
    for i in range(s,r):
        box =  min(capacity[i],deliever)
            
    for i in range(s,r):
        capacity[i]-=deliever
        
    ans+=deliever
    
print(ans)