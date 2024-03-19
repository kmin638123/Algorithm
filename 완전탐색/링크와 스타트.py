# 시간초과 풀이
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n = int(input())
# table = [list(map(int, input().split())) for _ in range(n)]

# ans = 1e9
# for i in range(n//2):
#     for start in combinations(range(n), i+1):
#         link = set(range(n)) - set(start)
#         # print(start, link)
        
#         s = l = 0
#         if len(start)!=1:
#             for two in combinations(start, 2):
#                 s+=(table[two[0]][two[1]]+table[two[1]][two[0]])
#         for two in combinations(link, 2):
#             l+=(table[two[0]][two[1]]+table[two[1]][two[0]])
#         # print(s, l)
#         ans = min(ans, abs(s-l))
        
# print(ans)
#############################################################
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

sum_stat = [sum(i) + sum(j) for i, j in zip(table, zip(*table))] 

total = sum(sum_stat) // 2 # 모든 값 합의 절반

ans = 1e9

for i in range(n//2):
    for l in combinations(sum_stat, i+1):
        # print(l)
        ans = min(ans, abs(total - sum(l))) # 모든 값의 절반 - 그 뽑은 2개 합의 차 = start팀 - link팀

print(ans)