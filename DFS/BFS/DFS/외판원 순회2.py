# TSP
# 시간 초과 풀이
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# ans = 1e9

# visited =[False] * n

# def dfs(arr):
#     global ans
#     if len(arr)==n and graph[arr[-1]][arr[0]]!=0:
#         cost = 0
#         arr = arr + [arr[0]]
#         for i in range(n):
#             cost+= graph[arr[i]][arr[i+1]]
#         ans = min(ans, cost)
#         return
#     for i in range(n):
#         if not visited[i]:
#             if len(arr)==0 or graph[arr[-1]][i]!=0:
#                 visited[i] = True
#                 dfs(arr+[i])
#                 visited[i] = False

# arr = []
# dfs(arr)
# print(ans)
#####################################################
# dfs로 넘겨줄 때, cost도 함께 넘겨보자    
# 틀린 풀이 (원인 불명,,,)
   
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# ans = 1e9

# visited =[False] * n

# def dfs(arr, cost):
#     global ans
#     if len(arr)==n and graph[arr[-1]][arr[0]]!=0:
#         cost += graph[arr[-1]][arr[0]]
#         ans = min(ans, cost)
#         return
    
#     for i in range(n):
#         if not visited[i]:
#             c = 0 if len(arr)==0 else cost+graph[arr[-1]][i]
#             visited[i] = True
#             dfs(arr+[i], c)
#             visited[i] = False
                
# arr = []
# dfs(arr,0)
# print(ans)


#####################################################
# dfs로 넘겨줄 때, start, init을 함께 넘겨보자    
           
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9

visited =[False] * n

def dfs(start, init):
    global ans
    if len(arr)==n-1 and graph[start][init]!=0:
        ans = min(ans, sum(arr)+graph[start][init])
        return
    
    for i in range(n):
        if not visited[i] and graph[start][i]!=0:
            visited[i] = True
            arr.append(graph[start][i])
            dfs(i,init)
            arr.pop()
            visited[i] = False
                
arr = []
for i in range(n):
    visited[i]=True
    dfs(i,i)
    visited[i]=False
print(ans)
            