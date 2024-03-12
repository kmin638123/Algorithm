import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        parent[x]=y

for i in range(1, n+1):
    edges = list(map(int, input().split()))
    for idx, e in enumerate(edges):

        if idx+1 == i:
            continue
        if e == 1:
            union(i,idx+1)

# print(parent)

plan = list(map(int, input().split()))
# check = 1
# for i in range(1,n):
#     if find(plan[i-1])!=find(plan[i]):
#         check = 0
#         break
# if check: print("YES")
# else: print("NO")

result = set([find(i) for i in plan])
if len(result) > 1: print('NO')
else: print('YES')