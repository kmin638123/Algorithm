# # 메모리 초과 풀이
# import sys
# from itertools import permutations

# input = sys.stdin.readline

# n = int(input())

# for _ in range(n):
#     s = sorted(list(input().rstrip()))
#     tmp = ''
#     for comb in permutations(s, len(s)):
#         now = "".join(comb)
#         if tmp==now:
#             continue
#         print(now)
############################################    
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

def dfs(alpha, ans):
    if len(ans) == len(s):
        print("".join(ans))
        return

    for x in alpha:
        if alpha[x]:
            ans.append(x)
            alpha[x]-=1
            dfs(alpha, ans)
            alpha[x]+=1
            ans.pop()


for _ in range(n):
    s = sorted(list(input().rstrip()))
    alpha = dict()
    
    for i in s:
        if i in alpha.keys():
            alpha[i]+=1
        else:
            alpha[i] =1
    
    dfs(alpha, [])