# 내 풀이
import sys

n = int(input())

tips = []
for _ in range(n):
    tips.append(int(sys.stdin.readline()))

tips.sort(reverse=True)

answer = 0
for i in range(n):
    if tips[i]>i:
        answer+=(tips[i]-i)
print(answer)
            
###############################
# 좀 더 간단히
n = int(input())
tips = [int(input()) for _ in range(n)]

answer = 0
for i, tip in enumerate(sorted(tips, reverse=True)):
    if tip-i>0:
        answer+=(tip-i)
print(answer)
            