# from itertools import combinations
# n, m = map(int, input().split())

# print(len(list(combinations(range(1,n+1),m))))
################################################
# nCm = n-1Cm-1 + n-1Cm

n, m = map(int, input().split())

dp = [[0]* (m+1) for _ in range(n+1)]

def combi(n,m):
    if n == 1 or n == m or m==0:
        return 1
    if dp[n][m]==0:
        dp[n][m]= combi(n-1, m-1)+combi(n-1, m)
    return dp[n][m]

print(combi(n,m))