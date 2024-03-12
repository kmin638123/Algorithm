import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

G = int(input())
P = int(input())


parent = [-1 for i in range(G+1)]

def find(x):
    if parent[x]<0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    
    parent[y] = x

ans = 0  
g = list(int(input()) for _ in range(P))
for g_i in g:
    # g = int(input())
    d = find(g_i)
    
    if d == 0: # 더 이상 도킹 X
        break 
    
    union(d-1,d) #a이전 게이트로 대안 설정
    ans+=1
    
print(ans)