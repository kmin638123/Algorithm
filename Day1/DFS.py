# 로또 문제
# 입력 받는 연습
def dfs(depth):
    if len(temp) == 6:
        print(*temp)
        return
    else:
        for i in range(depth, a):
            temp.append(b[i])
            dfs(i+1)
            temp.pop()

while True:
    array = list(map(int, input().split()))
    a = array[0]
    b = sorted(array[1:])
    temp = []
    dfs(0)

    if a == 0:
        break
    print()