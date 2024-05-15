import sys
input = sys.stdin.readline

h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
# 본인 위치를 기준으로 양 옆에 본인보다 높은 블록이 존재해야 본인 위치에 물이 고임
# 맨 앞과 뒤에는 물이 고일 수 없음
for i in range(1, w - 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare:
        ans += compare - world[i]

print(ans)