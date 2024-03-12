import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

parent = list(i for i in range(1000001))
size = list(1 for _ in range(1000001))

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    if x<y:
        parent[y] = x
        size[x]+=size[y]
        size[y]=0
    else:
        parent[x]=y
        size[y] += size[x]
        size[x]=0

for _ in range(n):
    i = list(input().split())
    if i[0]=="I":
        union(int(i[1]),int(i[2]))
    else:
        print(size[find(int(i[1]))])