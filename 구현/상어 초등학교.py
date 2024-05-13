import sys
import heapq
input = sys.stdin.readline

n = int(input())
seat = [[0] *n for _ in range(n)]
dx, dy = [0,1,0,-1], [-1,0,1,0]

def check(nums):
    s = nums[0]
    info = []
    
    for i in range(n):
        for j in range(n):
            like, blank = 0, 0 
            if not seat[i][j]: # 아직 배정되지 않은 칸인 경우
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if not seat[nx][ny]: blank-=1
                        else: like -= 1 if seat[nx][ny] in nums else 0
                heapq.heappush(info, (like, blank, i, j))     
    l, b, x, y = heapq.heappop(info)
    seat[x][y] = s
    return 

happy = dict()

for _ in range(n**2):
    nums = list(map(int, input().split()))
    happy[nums[0]] = nums[1:]
    check(nums)
ans = 0
for i in range(n):
    for j in range(n):
        likes =happy[seat[i][j]]
        cnt = 0
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if seat[nx][ny] in likes: cnt+=1
        ans+= int(10 ** (cnt-1))
        
print(ans)