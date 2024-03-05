# 내 풀이
n = int(input())
numbers = list(map(int, input().split()))

plus, minus, multi, div = map(int, input().split())

# 이렇게 하면 틀림,,,
# max_value = -1e9
# min_value = 1e9
max_value = -1000000001
min_value = 1000000001

def dfs(res, idx, plus, minus, multi, div):
    global max_value, min_value
    if idx == n:
        max_value = max(max_value, res)
        min_value = min(min_value, res)
        return
    
    if plus>0:
        dfs(res+numbers[idx],idx+1,plus-1,minus,multi, div)
    if minus>0:
        dfs(res-numbers[idx],idx+1,plus,minus-1,multi, div)
    if multi>0:
        dfs(res*numbers[idx],idx+1,plus,minus,multi-1, div)
    if div>0:
        dfs(int(res/numbers[idx]),idx+1,plus,minus,multi, div-1)
        
dfs(numbers[0], 1, plus, minus, multi, div)
print(max_value)
print(min_value)