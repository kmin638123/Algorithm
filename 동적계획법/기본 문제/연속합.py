import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]]

for i in range(1, n):
    dp.append(max(dp[-1]+nums[i],nums[i]))
    
print(max(dp))