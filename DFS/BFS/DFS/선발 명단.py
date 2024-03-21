import sys
input = sys.stdin.readline

c = int(input())

def dfs(ans):
    global answer
    members = len(ans) # 현재 정해진 인원
    if members==11:
        answer = max(answer, sum(ans))
        return 
    
    
    for i in range(11):
        # 이미 차지된 포지션 or 지금 멤버의 포지션 능력치가 0인 경우
        if visited[i] or arr[members][i]==0:
            continue
        visited[i] = True
        ans.append(arr[members][i])
        dfs(ans)
        visited[i] = False
        ans.pop()     
        
    

for _ in range(c):
    arr = [list(map(int, input().split())) for _ in range(11)]
    answer = 0
    visited = [False for _ in range(11)]

    dfs([])
    print(answer)