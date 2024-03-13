import sys
input = sys.stdin.readline

t = int(input())

def vps(x):
    cnt = 0
    for i in x:
        if i == "(":
            cnt+=1
        else:
            if cnt<=0: 
                return "NO"
            cnt-=1

    return "YES" if not cnt else "NO"

for _ in range(t):
    x = input().rstrip()
    print(vps(x))
    
    