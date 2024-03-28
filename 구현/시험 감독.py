import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

b, c = map(int, input().split())

ans = 0
for num in nums:
    if num>b:
        bu = (num-b)//c if (num-b)%c==0 else (num-b)//c+1
        ans+=bu
    ans+=1
print(ans)