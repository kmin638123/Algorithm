m = 4
n = 3

# n*m 배열 만들기
a = [[0] * m for _ in range(n)]
# print(a)

# 반복적으로 입력 받기
# 방학 숙제
L, A, B, C, D = [int(input()) for _ in range(5)]
# print(L-max(A//C+1 if A%C!=0 else A//C, B//D+1 if B%D!=0 else B//D))

# 2차원 배열 입력 받기
n, m = map(int, input().split()) # n*m 배열
# 1) 공백 없이 주어지는 경우
no_blank = [list(map(int, input())) for _ in range(n)]
# 2) 공백으로 구분되는 경우
yes_blank = [list(map(int, input().split())) for _ in range(n)]

# 빠른 입력 받기
# 빠른 A+B
import sys
T = int(sys.stdin.readline())
for i in range(T):
    fst, snd = map(int, sys.stdin.readline().split())
    print(fst+snd)
