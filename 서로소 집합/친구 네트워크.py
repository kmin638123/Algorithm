import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

t = int(input())


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
        parent[x] = y
        size[y] += size[x]
        size[x] = 0
    else:
        parent[y] =x
        size[x] += size[y]
        size[y] = 0

for _ in range(t):
    f = int(input())
    
    parent = [i for i in range(f*2)]
    size = [1 for i in range(f*2)]
    idx = dict()
    p = 0
    
    for _ in range(f):
        a, b = input().split()
        if not a in idx.keys():
            idx[a] = p
            p+=1
        if not b in idx.keys():
            idx[b] = p
            p+=1
        union(idx[a],idx[b])
        print(size[find(idx[a])])
        