import sys
input = sys.stdin.readline
n = int(input())
# first = [i for i in range(1,n+1)]
second =[0]+[int(input()) for _ in range(n)]

ans = set()

def dfs(idx, up, down):
    up.add(idx)
    down.add(second[idx])
    
    if second[idx] in up: # 
        if up == down: 
            ans.update(up)
        return
    
    return dfs(second[idx], up,down)

for i in range(n):
    if i+1 not in ans:
        dfs(i+1, set(), set())

print(len(ans))
for i in sorted(list(ans)):
    print(i)
