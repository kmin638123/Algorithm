# 내 풀이
n = int(input())
lost = list(map(int, input().split()))

lost.sort()

answer = lost[-1]

if len(lost)%2==1:
    lost = lost[:-1]
    n -= 1

for i in range(0, n//2):
    if answer < lost[i]+lost[n-i-1]:
        answer = lost[i]+lost[n-i-1]
print(answer)

#################################
n = int(input())
lost = list(map(int, input().split()))

lost.sort()

m = 0 
if len(lost)%2==1:
    m = lost.pop(-1)

a = [lost[i]+lost[-1-i] for i in range(len(lost)//2)]
a.append(m)

print(max(a))
