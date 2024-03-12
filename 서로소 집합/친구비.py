import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [0]+list(map(int, input().split()))

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] =i
    
def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        parent[x]=y
    a[y] = min(a[x],a[y])
        
for _ in range(m):
    v, w = map(int, input().split())
    union(v,w)
    # print(parent)
    
# cost = dict()

# for i in range(1, n+1):
#     if parent[i] in cost.keys():
#         cost[parent[i]] = min(a[i], cost[parent[i]])
#     else:
#         cost[parent[i]] = a[i]

# total = sum(list(cost.values()))

total = 0
for i in range(1, n+1):
    if parent[i]==i:
        total+=a[i]

if total <= k: print(total)
else: print("Oh no")