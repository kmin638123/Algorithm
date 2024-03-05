# 원소끼리 떨어져 있어도 부분수열!!!
# 내 풀이
n, s = map(int, input().split())
numbers = list(map(int, input().split()))

visited =[False] * n
arr = []

cnt = []
def dfs(arr,idx):
    if sum(arr)==s and len(arr)>0:
        cnt.append(arr)
    for i in range(n):
        if not visited[i] and idx<i:
            visited[i]=True
            dfs(arr+[numbers[i]],i)
            visited[i]=False
dfs(arr,-1)
print(len(cnt))


##################################
# 같은 풀이 더 간단하게

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
arr = []

def dfs(start):
    global cnt
    if sum(arr) == s and len(arr)>0:
        cnt+=1
    
    for i in range(start, n):
        arr.append(numbers[i])
        dfs(i+1)
        arr.pop()
        
dfs(0)
print(cnt)