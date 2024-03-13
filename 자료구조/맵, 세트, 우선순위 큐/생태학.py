import sys
input = sys.stdin.readline

d = dict()

total = 0
while True:
    tree = input().rstrip()
    if tree == "":
        break
    if tree in d:
        d[tree]+=1
    else:
        d[tree] =1
    total+=1

sd = dict(sorted(d.items()))

for i in sd:
    per = sd[i]/total * 100
    print("%s %.4f" %(i, per))