# 내 풀이
n = int(input())
price = [int(input()) for _ in range(n)]

answer = 0

for i, p in enumerate(sorted(price, reverse=True)):
    if (i)%3!=2:
        answer+=p
print(answer)

##########################
# 다른 풀이
n = int(input())
price = [int(input()) for _ in range(n)]

price.sort(reverse=True)

answer = 0
for i in range(2, len(price), 3):
    answer += price[i]
print(sum(price)-answer)
