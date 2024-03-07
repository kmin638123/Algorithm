# 수 정렬하기
n = int(input())
numbers = [int(input()) for _ in range(n)]
print(*sorted(numbers))

###########################################
# 수 정렬하기 2 - 위처럼 하면 시간 초과 뜸!
#  삽입 정렬을 한 번 써보자 => 시간 초과,,,
# n = int(input())
# numbers = [int(input()) for _ in range(n)]

# for i in range(n):
#     for j in range(i,0,-1):
#         if numbers[j]<numbers[j-1]:
#             numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
#         else:
#             break
# for i in numbers:
#     print(i, end="\n")

# nlogn의 시간 복잡도 알고리즘을 써야 함
# input()이 아니라 sys.stdin.readline() 써야 함...
import sys

n = int(input())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

def merge_sort(arr):
    if len(arr)<2:
        return arr
    
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    
    return merge(low_arr, high_arr)

def merge(left, right):
    merged_arr = []
    l = h = 0
    while l<len(left) and h<len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l+=1
        else:
            merged_arr.append(right[h])
            h+=1
    
    merged_arr+=(left[l:])
    merged_arr+=(right[h:])
    return merged_arr

for i in merge_sort(numbers):
    print(i,end="\n")
    
###########################################  
# 수 정렬하기 3
# 병합 정렬을 사용하면 메모리 초과가 뜬다.
# 계수 정렬 사용!
import sys

n = int(input())

count = [0] * 10001

for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    count[m]+=1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end="\n")


