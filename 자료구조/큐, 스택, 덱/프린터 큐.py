from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    l = [i for i in range(n)]
    queue = deque(l)
    im = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        d[i] = im[i]
    ans = 1
    while True:
        p = queue.popleft()
        if d[p] == max(d.values()):
            if p == m:
                print(ans)
                break
            d.pop(p)
            ans+=1
        else:
            queue.append(p)