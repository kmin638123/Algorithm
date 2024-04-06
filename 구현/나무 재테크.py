# 파이썬 시간 초과 풀이
# import sys
# # from collections import deque
# input = sys.stdin.readline

# n, m, k = map(int, input().split())

# A = [list(map(int, input().split())) for _ in range(n)]
# a = [[5] * n for _ in range(n)]

# land = [[list() for _ in range(n)] for _ in range(n)]
# # land = [[list()]* n for _ in range(n)] => 이렇게 하면 안됨ㅍ

# for _ in range(m):
#     x, y, z = map(int, input().split())
#     land[x-1][y-1].append(z)

# for i in range(n):
#     for j in range(n):
#         land[i][j].sort()

# dx = [-1,-1,-1,0,0,1,1,1]
# dy = [-1,0,1,-1,1,-1,0,1]

# for _ in range(k): # k년 반복
#     for i in range(n):
#         for j in range(n):
#             die = -1
#             if land[i][j]: # 봄
#                 for idx, tree in enumerate(land[i][j]):
#                     if tree>a[i][j]:
#                         die = idx
#                         break
#                     else:
#                         a[i][j]-=tree
#                         land[i][j][idx]+=1
#                 # 여름 
#                 if die !=-1:
#                     a[i][j] += (sum(map(lambda x:x//2, land[i][j][die:])))
#                     land[i][j] = land[i][j][:die]
                    
#     for i in range(n):
#         for j in range(n):            
#                 # 가을
#                 for tree in land[i][j]:
#                     if tree>=5 and tree%5==0:
#                         for idx in range(8):
#                             nx = i+dx[idx]
#                             ny = j+dy[idx]
#                             if 0<=nx<n and 0<=ny<n:
#                                 land[nx][ny] = [1] + land[nx][ny]
                                
                                                        
#     # 겨울
#     for i in range(n):
#         for j in range(n):
#             a[i][j] += A[i][j]
# ans = 0
# for i in range(n):
#     for j in range(n):
#         if land[i][j]:
#             ans+=len(land[i][j])
            
# print(ans)


#################################################
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
a = [[5] * n for _ in range(n)]

land = [[{} for _ in range(n)] for _ in range(n)]
# land = [[list()]* n for _ in range(n)] => 이렇게 하면 안됨ㅍ

for _ in range(m):
    x, y, z = map(int, input().split())
    land[x-1][y-1][z] = 1

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for _ in range(k): # k년 반복
    for i in range(n):
        for j in range(n):
            if land[i][j]: # 봄, 여름
                die = False
                updated_tree = {}
                for idx,age in enumerate(sorted(land[i][j].keys())):
                    tree = land[i][j][age] # 해당 age인 tree 개수
                    if die: # 살 수 있는 나무 없음
                        a[i][j]+= tree * (age//2)
                    elif tree*age<= a[i][j]: # 해당 age인 tree들이 모두 자랄 수 있을 때
                        updated_tree[age+1] = tree # 해당 age인 tree 모두 한 살씩 자람
                        a[i][j]-=tree*age
                    else:
                        # 자랄 수 있는 나무 개수 구하기
                        grow, remain = divmod(a[i][j],age)
                        a[i][j] = remain + (tree-grow) * (age//2)
                        if grow>0: # 나무가 한 개 이상 자랄 수 있다면
                            updated_tree[age+1] = grow
                        die = True
                land[i][j] = updated_tree
    # 가을
    for i in range(n):
        for j in range(n):            
            # 번식할 나무 개수
            new = 0
            for age in land[i][j].keys():
                if age>=5 and age%5==0:
                    new += land[i][j][age]
            if new>0:
                for idx in range(8):
                    nx = i+dx[idx]
                    ny = j+dy[idx]
                    if 0<=nx<n and 0<=ny<n:
                        if 1 in land[nx][ny]: # 1살 나무가 존재하는 경우
                            land[nx][ny][1]+=new
                        else:
                            land[nx][ny][1] = new
            a[i][j] += A[i][j]


print(sum(sum(sum(col.values()) for col in row) for row in land))
