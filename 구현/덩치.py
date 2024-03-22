import sys
input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

ans = []

for i in range(n):
    me = people[i]
    rank = 1
    for j in range(n):
        if i==j:
            continue
        other = people[j]
        if me[0]<other[0] and me[1]<other[1]:
            rank+=1
    print(rank, end=" ")