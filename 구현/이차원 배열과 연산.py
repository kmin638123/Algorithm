import sys
from collections import Counter
input = sys.stdin.readline

r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]

time = 0

def RC(rc):
    sorted = []
    l = 0
    for row in a:
        count = dict()
        for col in row:
            if col!=0:
                if col in count:
                    count[col] += 1
                else:
                    count[col] = 1
        count = list(count.items())
        count.sort(key= lambda x: (x[1],x[0]))
        tmp = sum(count, ())
        l = max(l, len(tmp))
        sorted.append(list(tmp))
        
    if l>100:
        l = 100
            
    for i in sorted:
        i+=[0] * (l-len(i))
         
    return sorted if rc else list(zip(*sorted))
   
      
while True:
    
    if (len(a)>r-1 and len(a[0])>c-1 and a[r-1][c-1] == k) or time>100:
        break
    if len(a) >= len(a[0]): # R 연산
        a = RC(1)
    else:
        a = list(zip(*a))
        a = RC(0)

    time+=1

print(time if time<=100 else -1)