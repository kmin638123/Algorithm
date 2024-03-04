# 내 풀이
import sys
n = int(input())
drinks = list(map(int, sys.stdin.readline().split()))

drinks.sort(reverse=True)
result = drinks[0]

for i in range(1, n):
    result += (drinks[i]/2)
    
print(result)