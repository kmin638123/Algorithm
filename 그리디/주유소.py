import sys
n = int(input())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

# 제일 싼 가격의 오일로 쭈욱 넣으면 됨!
# 더 싼 가격의 오일이 나올 때마다 새로 주유하면 됨!
oil = price[0]
result = 0
for i in range(n-1):
    if price[i]<oil:
        oil = price[i]
    result += road[i]*oil
print(result)