# 피보나치 수, 피보나치 수 2, 피보나치 수 4, 피보나치 수 5
# 재귀 => 시간 초과
# n = int(input())
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(n))

n = int(input())
fibonacci = [0,1]
for i in range(2,n+1):
    num = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(num)
print(fibonacci[n])

#############################################
# 피보나치 수 3
# 피사노 주기: 피보나치 수를 m으로 나눈 나머지는 항상 주기를 갖게 된다.
# m = 10^k일 때, k>2라면, 주기는 항상 15*(10^(k-1))이다.

n = int(input())
fibonacci = [0,1]

p = n%((10**5)*15)

for i in range(2,p+1):
    num = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(num)
    fibonacci[i] %= 1000000
    
print(fibonacci[p])
