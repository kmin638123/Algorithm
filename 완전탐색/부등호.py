import sys
input = sys.stdin.readline

k = int(input())
arr = input().split()

ans = []

def dfs(nums):
    idx = len(nums)
    if idx==k+1:
        ans.append(int("".join(nums)))
        return
    giho = arr[idx-1] # 부등호 어떤 거인지
    
    for i in range(10):
        if str(i) not in nums and eval(nums[-1]+giho+str(i)):
            dfs(nums+[str(i)])

for i in range(10):
    dfs([str(i)])

print(ans[-1])
if len(str(ans[0]))==k:
    print("0"+str(ans[0]))
else:
    print(ans[0])