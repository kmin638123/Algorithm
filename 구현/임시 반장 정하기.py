import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
grade = list(zip(*arr)) # grade 별 

std, ans = n,0

for i in range(n):
    friend = set() # 학생 별 같은 반 친구
    for j in range(5):
        for k in range(len(grade[j])):
            if i==k:
                continue
            else:
                if grade[j][k]==arr[i][j]: 
                    friend.add(k)
    # print(friend)
    if ans == len(friend):
        if i < std:
            std = i
    elif ans<len(friend):
        std = i
        ans = len(friend)

print(std+1)
    