import sys

n = int(input())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
m = int(input())
nums = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end = mid -1
        else:
            start = mid+1
    return -1

for num in nums:
    check = binary_search(cards, num, 0, n-1)
    if check!=-1:
        print(1, end=" ")
    else:
        print(0, end=" ")