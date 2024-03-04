# 내 풀이
a, b = map(int, input().split())

cnt = 0
while a<b:
    if b%2==0:
        b = b//2
        cnt+=1
    elif b%10==1:
        b=b//10
        cnt+=1
    else:
        cnt = -2
        break

if a!=b:
    cnt = -2
print(cnt+1)
    