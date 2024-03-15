a, b, c, m = map(int, input().split())
t = 0 
w = 0

for i in range(24):
    if t+a <= m:
        t += a
        w+=b
    else:
        if t-c>=0:
            t-=c
        else:
            t = 0

print(w)