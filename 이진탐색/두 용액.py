import sys
input = sys.stdin.readline

n = int(input())
value = list(map(int, input().split()))

value.sort()

res  = 1e9 * 2 + 1
idx1 = idx2 = 0

for i in range(n-1):
    start, end = i+1, n-1
    
    while start<=end:
        mid = (start+end)//2
        s = value[i] + value[mid]
        
        if s<0:
            start = mid+1
        else:
            end = mid-1

        if res > abs(s):
            res = abs(s)
            idx1, idx2 = i, mid
            
print(value[idx1], value[idx2])
