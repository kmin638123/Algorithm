############# (1) #############
n, m = map(int, input().split())

answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        answer.append(arr)
        return 
    for i in range(1,n+1):
        if i not in arr:
            dfs(arr+[i])

dfs(arr)
for a in answer:
    for i in range(m):
        print(a[i], end=" ")
    print(end="\n")
    
############# (2) #############
n, m = map(int, input().split())

answer = []
arr =[]

def dfs(arr):
    if len(arr)==m:
        answer.append(arr)
        return 
    for i in range(1,n+1):
        if len(arr)==0 or arr[-1]<i:
            dfs(arr+[i])

dfs(arr)
for a in answer:
    for i in range(m):
        print(a[i], end=" ")
    print(end="\n")

############# (3) #############
n, m = map(int, input().split())

answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        answer.append(arr)
        return 
    for i in range(1,n+1):
        dfs(arr+[i])

dfs(arr)
for a in answer:
    for i in range(m):
        print(a[i], end=" ")
    print(end="\n")

############# (4) #############
n, m = map(int, input().split())

answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        answer.append(arr)
        return 
    for i in range(1,n+1):
        if len(arr)==0 or arr[-1]<=i:
            dfs(arr+[i])

dfs(arr)
for a in answer:
    for i in range(m):
        print(a[i], end=" ")
    print(end="\n")

############# (5) #############   
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        answer.append(arr)
        return 
    for i in l:
        if i not in arr:
            dfs(arr+[i])

dfs(arr)
for a in answer:
    for i in range(m):
        print(a[i], end=" ")
    print(end="\n")
    
############# (6) #############   
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        answer.append(arr)
        return 
    for i in l:
        if len(arr)==0 or arr[-1]<i:
            dfs(arr+[i])

dfs(arr)
for a in answer:
    for i in range(m):
        print(a[i], end=" ")
    print(end="\n")
    
############# (7) #############   
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        answer.append(arr)
        return 
    for i in l:
        dfs(arr+[i])

dfs(arr)
for a in answer:
    for i in range(m):
        print(a[i], end=" ")
    print(end="\n")
    
############# (8) #############   
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        answer.append(arr)
        return 
    for i in l:
        if len(arr)==0 or arr[-1]<=i:
            dfs(arr+[i])

dfs(arr)
for a in answer:
    for i in range(m):
        print(a[i], end=" ")
    print(end="\n")
    
    
############# (9) #############   
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

visited = [False] * n
answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        print(*arr)
        return 
    tmp = 0
    for i in range(n):
        if not visited[i] and tmp!=l[i]:
            visited[i] = True
            tmp = l[i]
            dfs(arr+[l[i]])
            visited[i] = False

dfs(arr)

############# (10) ############# 
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

visited = [False] * n
answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        print(*arr)
        return 
    tmp = 0
    for i in range(n):
        if not visited[i] and tmp!=l[i]:
            if len(arr)==0 or arr[-1]<=l[i]:
                visited[i] = True
                tmp = l[i]
                dfs(arr+[l[i]])
                visited[i] = False

dfs(arr)

############# (11) ############# 
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        print(*arr)
        return 
    tmp = 0
    for i in range(n):
        if tmp!=l[i]:
            tmp = l[i]
            dfs(arr+[l[i]])

dfs(arr)

############# (12) ############# 
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

answer = []
arr = []

def dfs(arr):
    if len(arr)==m:
        print(*arr)
        return 
    tmp = 0
    for i in range(n):
        if tmp!=l[i]:
            if len(arr)==0 or arr[-1]<=l[i]:
                tmp = l[i]
                dfs(arr+[l[i]])

dfs(arr)
