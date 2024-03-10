# 틀린 풀이
# x = int(input())

# dp = [0,0]

# for i in range(2,x+1):
#     if i%3==0:
#         dp.append(min(dp[i//3],dp[i-1])+1)
#     elif i%2==0:
#         dp.append(min(dp[i//2],dp[i-1])+1)
#     else:
#         dp.append(dp[i-1]+1)
# print(dp[x])

###################################################
x = int(input())

dp = [0,0]

for i in range(2,x+1):
    d = dp[i-1]
    if i%3==0:
        d = min(d, dp[i//3])
    if i%2==0: # elif가 아니라 if로 해야 함
        d = min(d, dp[i//2])
    dp.append(d+1)
    
print(dp[x])