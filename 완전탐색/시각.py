n, k = input().split()

ans = 0

for i in range(0, int(n)+1):
    if k == '0' and i<10:
        ans+=3600
        continue
    if k in str(i):
        ans+=3600
        continue
    for j in range(0, 60):
        if k=='0' and 1<=j<=9:
            ans+=60
            continue
        if k in str(j):
            ans+=60
            continue
        for K in range(0, 60):
            if k=='0' and 1<=K<=9:
                ans+=1
                continue
            if k in str(K):
                ans+=1
                
print(ans)