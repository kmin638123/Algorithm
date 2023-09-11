n = int(input())
a=[]

for _ in range(n):
    name, kor, eng, math = input().split()
    a.append([name, int(kor), int(eng), int(math)])

a.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for x in a:
    print(x[0])