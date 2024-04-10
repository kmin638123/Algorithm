import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 1
for x in range(n-1):
    for z in range(n-1,-1,-1):
        if z<x+1:
            continue
        # 세 수가 있으면, 작은 수 + 그 다음 작은 수 > 가장 큰 수 관계를 만족하면
        # 삼각관계가 만족된다!
        # 따라서, 최대한 많은 범위를 지키려면, 작은 두 수는 0 부터 x, x+1으로 설정
        # 가장 큰 수는 n-1 부터 앞쪽으로 가면서 확인하면 된다
        if arr[x]+arr[x+1]>arr[z]:
            ans = max(z-x+1, ans)
            continue
            
print(ans)