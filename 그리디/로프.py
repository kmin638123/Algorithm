## 내 풀이
import sys

n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(sys.stdin.readline()))
    
ropes.sort(reverse=True)

m = ropes[0] # 최대 중량

for i in range(1,n):
    parallel = ropes[i] * (i+1)
    if m < parallel:
        m = parallel
        
    # break를 하면 안됨..! 
    # else:
    #     break
    
print(m)

##############################
# 비교를 하지 않고, 리스트에 저장해두는 풀이
n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)
result = []

for j in range(n):
    result.append(ropes[j]*(j+1))
print(max(result))