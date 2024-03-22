# 분해합: 가장 작은 생성자를 구해내는 프로그램 작성
# n = int(input())

# for i in range(n):
#     tmp = i + sum(map(int,str(i)))
#     if tmp == n:
#         print(i)
#         exit()
        
# print(0)
####################################################
# 셀프 넘버
self_number = [0] * (10001)
for i in range(1,10000):
    num = i +sum(map(int, str(i)))
    if num<=10000:
        self_number[num]=1
    if self_number[i]==0:
        print(i)
        