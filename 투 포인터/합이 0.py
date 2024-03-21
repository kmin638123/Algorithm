from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

ans = 0
for i in range(n-2):
    j = i+1
    k = n-1
    while j<k:
        s = arr[i]+arr[j]+arr[k]

        if s==0:
            if arr[j] == arr[k]:
                ans += (k-j)
            else:
                idx = bisect_left(arr, arr[k])
                ans += (k+1-idx)
            j+=1
        elif s<0:
            j+=1
        else:
            k-=1
print(ans)