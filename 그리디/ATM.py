# 내 풀이
import sys

n = int(input())
time = list(map(int, sys.stdin.readline().split()))

answer = 0
for i, t in enumerate(sorted(time)):
    answer+=(t*(n-i))
    
print(answer)

##############################
# 다른 풀이
n = int(input())
time = list(map(int, input().split()))

time.sort()

answer = 0
for i in range(1, n+1):
    answer+=sum(time[:i])
    
print(answer)