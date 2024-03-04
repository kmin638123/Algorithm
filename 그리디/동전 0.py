# 내 풀이
n, k = map(int, input().split())
coins = []
for _ in range(n):
    c = int(input())
    if c<=k:
        coins.append(c)
coins.sort(reverse=True)

i = 0
cnt = 0
while k!=0:
    cnt += k//coins[i]
    k = k-(k//coins[i])*coins[i]

    i+=1
print(cnt)

############################
# 동전들이 항상 배수관계이므로, 나머지로 k를 할당해도 된다.

n, k = map(int, input().split())
coins = []
for _ in range(n):
    c = int(input())
    if c<=k:
        coins.append(c)
coins.sort(reverse=True)

cnt = 0
for i in coins:
    cnt += k //i
    k = k % i
print(cnt)