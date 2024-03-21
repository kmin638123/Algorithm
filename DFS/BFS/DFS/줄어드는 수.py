n = int(input())

arr = []
res = set()

def dfs():
    if len(arr)>0:
        res.add(int("".join(map(str, arr))))
        
    
    for i in range(10):
        if len(arr)==0 or arr[-1]>i:
            arr.append(i)
            dfs()
            arr.pop()

try:
    dfs()
    res = sorted(list(res))
    print(res[n-1])
except:
    print(-1)