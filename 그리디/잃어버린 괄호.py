# 내 풀이

s = input()
l = s.split("-")

# 0이 선행으로 나왔기 때문에 eval을 쓰면 오류!
# answer = eval(l[0])
# for i in range(1, len(l)):
#     answer-=eval(l[i])
    
answer = 0
for i, x in enumerate(l):
    for j in x.split("+"):
        if i == 0:
            answer += int(j)
        else:
            answer -= int(j)

print(answer)