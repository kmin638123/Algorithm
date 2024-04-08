import sys
input = sys.stdin.readline

a, b= map(int, input().split())

arr = [0] * (b+1)

cnt, now = 0,1
for i in range(1,b+1):
    arr[i] = now
    cnt+=1
    if cnt==now:
        cnt = 0 
        now+=1
print(sum(arr[a:b+1]))

##################################3
# 다른 사람 풀이

a,b = map(int,input().split())
 
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
print(sum(arr[a:b+1]))