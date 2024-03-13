# 다시 풀기

n, k = map(int, input().split())

people = [i+1 for i in range(n)]

y = []
num = 0 
for t in range(n):
    num += k-1  
    if num >= len(people):
        num = num%len(people)
 
    y.append(str(people.pop(num)))
    
print("<"+", ".join(y)+">")