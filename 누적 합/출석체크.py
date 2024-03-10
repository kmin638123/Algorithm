import sys
input = sys.stdin.readline
n, k, q, m = map(int, input().split())

sleep = [False for _ in range(n+3)]
for i in map(int, input().split()):
    sleep[i] = True

check = [1 for _ in range(n+3)]

for i in map(int, input().split()):
    if sleep[i]:
        continue
    for j in range(i, n+3, i):
        if sleep[j]:
            continue
        check[j] = 0

for _ in range(m):
    s, e = map(int, input().split())
    print(sum(check[s:e+1]))