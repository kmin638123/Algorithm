# 로또 문제
# 입력 받는 연습
# def dfs(depth):
#     if len(temp) == 6:
#         print(*temp)
#         return
#     else:
#         for i in range(depth, a):
#             temp.append(b[i])
#             dfs(i+1)
#             temp.pop()
#
# while True:
#     array = list(map(int, input().split()))
#     a = array[0]
#     b = sorted(array[1:])
#     temp = []
#     dfs(0)
#
#     if a == 0:
#         break
#     print()
####################################################
# 연산자 끼워넣기
# import sys
#
# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
# plus, minus, multi, divide = map(int, sys.stdin.readline().split())
#
# max_value = -1000000001
# min_value = 1000000001
#
# def dfs(num, idx, plus, minus, multi, divide):
#     global max_value, min_value
#     if idx == n:
#         max_value = max(max_value, num)
#         min_value = min(min_value, num)
#         return
#
#     if plus > 0:
#         dfs(num+numbers[idx],idx+1,plus-1,minus, multi, divide)
#     if minus > 0:
#         dfs(num-numbers[idx],idx+1,plus,minus-1, multi, divide)
#     if multi > 0:
#         dfs(num*numbers[idx],idx+1,plus,minus, multi-1, divide)
#     if divide > 0:
#         dfs(int(num/numbers[idx]),idx+1,plus,minus, multi, divide-1)
#
# dfs(numbers[0],1,plus, minus, multi, divide)
# print(max_value)
# print(min_value)
####################################################


