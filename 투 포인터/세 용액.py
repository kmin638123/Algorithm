import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

value = 4000000001  # 세 용액이라 ㅋㅋ
ans = []

for i in range(n-2):
    j, k = i+1, n-1
    while j < k:
        s = arr[i]+arr[j]+arr[k]
        if abs(s)<value:
            value = abs(s)
            ans = [arr[i],arr[j],arr[k]]
            if value == 0:
                print(*ans)
                exit()
        if s<0:
            j+=1
        else:
            k-=1

print(*ans)
