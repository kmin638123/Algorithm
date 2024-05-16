import sys
input = sys.stdin.readline

n = int(input())

blocks = [(0,0,0,0)]
for i in range(1, n+1):
    a, h, w = map(int, input().split())
    blocks.append((i,a,h,w))

blocks.sort(key= lambda x: (x[3])) # 가벼운 무게 순으로 정렬

dp = [0] * (n+1) # 인덱스가 i인 벽돌을 가장 아래에 두었을 때의 높이
for i in range(1, n+1):
    for j in range(0,i):
        if blocks[i][1]>blocks[j][1]:
            dp[i] = max(dp[i], dp[j]+blocks[i][2])


max_value = max(dp)
idx = n
res = []

while idx>0:
    if max_value == dp[idx]:
        res.append(blocks[idx][0])
        max_value-=blocks[idx][2]
    idx-=1

print(len(res))

for i in range(len(res)-1,-1,-1):
    print(res[i])

