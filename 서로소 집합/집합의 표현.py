import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x!= y:
        parent[x]=y    

for _ in range(m):
    c, a, b = map(int, input().split())
    if not c: 
        union(a,b)
    else:
        if find(a)!=find(b):
            print("no")
        else:
            print("yes")
        