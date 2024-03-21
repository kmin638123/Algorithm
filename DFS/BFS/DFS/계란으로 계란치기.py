import sys
input = sys.stdin.readline

n = int(input())
egg = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def dfs(idx, cnt):
    global ans
 
    # print(idx, cnt, egg)
    
    if idx == n:
        ans = max(ans, cnt)
        return
        
    if egg[idx][0]<=0: # 손에 든 계란이 깨진 경우
        dfs(idx+1, cnt)
        return
    check = 0 
    for i in range(n):
        if i == idx or egg[i][0]<=0:
            continue
        check = 1
        egg[i][0]-=egg[idx][1]
        egg[idx][0]-=egg[i][1]
        tmp = 0
        if egg[i][0]<=0:
            tmp+=1
        if egg[idx][0]<=0:
            tmp+=1
        dfs(idx+1, cnt+tmp)
        egg[i][0]+=egg[idx][1]
        egg[idx][0]+=egg[i][1]
        
    if not check: # 본인만 빼고 다 깨져있던 경우
        ans = max(ans, cnt)
        return

dfs(0,0)
print(ans)