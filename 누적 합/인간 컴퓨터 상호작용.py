# 인간-컴퓨터 상호작용
# 50점 풀이,,,
# import sys
# input = sys.stdin.readline

# s = input()
# n = int(input())

# alpha = 'abcdefghijklmnopqrstuvwxyz'

# char = dict()

# for i in alpha:
#     char[i]= [0]
#     cnt = 0
#     for j in range(len(s)):
#         if s[j]==i:
#             cnt = cnt+1
#         char[i].append(cnt)

# for _ in range(n):
#     a, l, r = sys.stdin.readline().split()
#     print(char[a][int(r)+1]-char[a][int(l)])
#############################################

import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())

count = {0: [0]*26}
for i, ch in enumerate(s):
    count[i+1] = count[len(count)-1][:] # 이전 리스트 복사
    count[i+1][ord(ch)-97] += 1
    

for _ in range(n):
    a, l, r = sys.stdin.readline().split()
    print(count[int(r)+1][ord(a)-97]-count[int(l)][ord(a)-97])
