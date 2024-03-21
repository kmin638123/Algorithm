import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

l.sort()

i, j = 0, n-1

ans = [l[i], l[j]]
value = abs(l[i]+l[j])

while i<j:
    s = l[i]+l[j]
    if abs(s) < value:
        value = abs(s)
        ans = [l[i], l[j]]
        if value == 0:
            break
    if s<0:
        i+=1
    else:
        j-=1
print(*ans)