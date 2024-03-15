n = int(input())

for i in range(1, n+1):
    s = sum(map(int,str(i)))
    if s+i == n:
        print(i)
        exit()
    
print(0)
    