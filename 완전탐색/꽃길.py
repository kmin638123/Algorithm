from itertools import combinations

import sys
input = sys.stdin.readline

n = int(input())

ground = [list(map(int, input().split())) for _ in range(n)]

graph =[] # 테두리 제외

for i in range(1, n-1):
    for j in range(1,n-1):
        graph.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,-1,1]
ans = 1e9
for seeds in combinations(graph, 3):
    tmp = []
    price = 0
    check = 1
    
    for seed in seeds:
        if seed in tmp:
            price = 1e9
            break
        tmp.append(seed)
        price += ground[seed[0]][seed[1]]
        for i in range(4):
            nx = seed[0] +dx[i]
            ny = seed[1] +dy[i]
            if (nx,ny) in tmp:
                check = 0
                price = 1e9
                break
            tmp.append((nx,ny))
            price += ground[nx][ny]
        if not check:
            break
    
    ans = min(ans, price)
        
print(ans)