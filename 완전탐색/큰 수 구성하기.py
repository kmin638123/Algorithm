from itertools import product

n, K = map(int, input().split())
k = list(map(int, input().split()))

res = 0

for i in range(1,len(str(n))+1): # K+1로 하면 안됨!!!!
    for num in list(product(k,repeat=i)):
        num = int(''.join(map(str, num)))
        if num <= n:
            res = max(res, num)

print(res)
# print(list(product(k,repeat = 2)))