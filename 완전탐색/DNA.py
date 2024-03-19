import sys
n, m = map(int, input().split())

DNA = list(sys.stdin.readline().rstrip() for _ in range(n))


ans = ''
cnt = 0

for i in range(m):
    tmp = {"A":0,"T":0,"G":0, "C":0}
    for new in tmp.keys():
        # print(new)
        for dna in DNA:
            if dna[i]!=new:
                tmp[new]+=1
    tmp = sorted(tmp.items(), key= lambda x:(x[1],x[0]))[0]
    ans+=tmp[0]
    cnt+=tmp[1]
    
print(ans)
print(cnt)