import sys
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())

sticker = [list(map(int, input().split())) for _ in range(n)]

res = 0

for i in range(n):
    for j in range(i+1,n):
        h1, w1 = sticker[i]
        h2, w2 = sticker[j]
        tmp = h1 * w1 + h2 * w2
        
        # 둘 다 회전하지 않은 경우
        if (max(h1,h2)<=h and w1+w2<=w) or (max(w1,w2)<=w and h1+h2<=h):
            res = max(tmp,res)
            continue
        # i 스티커만 회전한 경우
        if (max(w1, h2)<=h and w2+h1<=w) or (max(h1, w2)<=w and h2+w1<=h):
            res = max(tmp, res)
            continue
        # j 스티커만 회전한 경우
        if (max(h1, w2)<=h and w1+h2<=w) or (max(w1, h2)<=w and h1+w2<=h):
            res = max(tmp, res)
            continue
        # 둘 다 회전한 경우
        if (max(w1, w2)<=h and h1+h2<=w) or (max(h1, h2)<=w and w1+w2<=h):
            res = max(tmp, res)
            continue
print(res)