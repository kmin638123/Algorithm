import sys
input = sys.stdin.readline

n, l = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def check(idx, d):
    used = []
    if d == 0:
        tmp = graph[idx][0]
        cnt = 1
        for i in range(1,n):
            if tmp == graph[idx][i]:
                cnt+=1
            elif tmp -1 == graph[idx][i]:
                for j in range(l-1):
                    used.append(i)
                    i+=1
                    if i >= n or tmp-1!=graph[idx][i]:
                        return False
                tmp = graph[idx][i]
                used.append(i)
                cnt = 1
            elif tmp + 1 == graph[idx][i]:
                if cnt<l or i-l in used:
                    return False
                tmp = graph[idx][i]
                cnt = 1
            else:
                return False
        return True
    else:
        tmp = graph[0][idx]
        cnt = 1
        for i in range(1,n):
            if tmp == graph[i][idx]:
                cnt+=1
            elif tmp -1 == graph[i][idx]:
                for j in range(l-1):
                    used.append(i)
                    i+=1
                    if i >= n or tmp-1!=graph[i][idx]:
                        return False
                tmp = graph[i][idx]
                cnt = 1
                used.append(i)
            elif tmp + 1 == graph[i][idx]:
                if cnt<l or i-l in used:
                    return False
                tmp = graph[i][idx]
                cnt = 1
            else:
                return False
        return True
        

ans = 0
for i in range(n):
    if check(i,0):
        ans+=1
    if check(i,1):
        ans+=1
        
print(ans)