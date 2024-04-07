import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

total = sum(sum(row) for row in a)

ans = 1e9

def calculate(x,y,d1,d2):
    first, second, third, fourth = 0,0,0,0
    # 1번 선거구
    one = y
    for r in range(x+d1):
        if r>=x:
            one-=1
        first+=sum(a[r][:one+1])
    
    # 2번 선거구
    two = y+1
    for r in range(x+d2+1):
        if r>x:
            two+=1
        second+=sum(a[r][two:])
        
    # 3번 선거구
    three = y - d1
    for r in range(x+d1,n):
        third+=sum(a[r][:three])
        if r<x+d1+d2:
            three+=1
        
    # 4번 선거구
    four = y + d2
    for r in range(x+d2+1,n):
        fourth+=sum(a[r][four:])
        if r<=x+d1+d2:
            four-=1    
            
    fifth = total - (first+second+third+fourth)
    
    return max(first, second, third, fourth, fifth)-min(first, second, third, fourth, fifth)
   
    
# 기준점과 경계 길이를 먼저 설정해주고 계산해줘야 함
for x in range(n-2):
    for y in range(1, n-1):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if x+d1+d2>n-1:
                    continue
                if 0>y-d1:
                    continue
                if n-1<y+d2:
                    continue
                ans = min(ans,calculate(x, y, d1, d2))

print(ans)