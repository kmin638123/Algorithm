import sys
n = int(input())
k = int(input())

sensor = list(map(int, input().split()))

sensor.sort()

if n<=k:
    print(0)
    exit()
    
dist = []
for i in range(1, n):
    dist.append(sensor[i]-sensor[i-1])
    
dist.sort(reverse=True)
print(sum(dist[k-1:])) # 가장 큰 간격 k-1개 제외