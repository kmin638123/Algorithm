# 내 풀이
# 일단 하나의 색을 쭉 칠하는 게 최소 횟수?
n = int(input())
color = input()
answer = 1
if "B" not in color or "R" not in color:
    print(answer)
else:
    r = 0
    b = 0
    tmp = color[0]
    for i in color[1:]:
        if tmp!=i:
            if i == "B":
                r+=1
            else:
                b+=1
            tmp = i
    if tmp=="B": b+=1
    else: r+=1
    
    print(min(b,r)+1)
#####################################
# 딕셔너리 이용
n = int(input())
color = input()

colors = {'B':0, 'R':0}
# 처음 색깔 칠하기
colors[color[0]]+=1

# 다른 색 나오면 해당 색 칠하는 횟수+1
for i in range(1,n): 
    if color[i] != color[i-1]:
        colors[color[i]]+=1

print(min(colors['B'], colors['R'])+1)