import sys
input = sys.stdin.readline

n = int(input())
susik = list(input().rstrip())
ans = -1e9 # 음수 값도 나올 수 있기 때문에, 이 점 유의!!!!

def dfs(idx, val):
    global ans
    if idx==n:
        ans = max(ans, int(val))
        return
    if idx+4<=n: # 괄호 사용
        # idx 말고, idx+2 의 연산자를 먼저 수행한다는 거임
        new = [val, susik[idx]]+[str(eval("".join(susik[idx+1:idx+4])))]
        dfs(idx+4, str(eval("".join(new))))
    if idx+2<=n: # 괄호 사용 x
        dfs(idx+2, str(eval("".join([val]+susik[idx:idx+2]))))

dfs(1, susik[0])
print(ans)