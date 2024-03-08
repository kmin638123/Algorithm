n = int(input())

def binary_search(start, end):
    while start<=end:
        mid = (start+end)//2
        if mid ** 2 == n:
            return mid
        elif mid ** 2 > n:
            end = mid-1
        else:
            start = mid+1
    return start

print(binary_search(0,n))