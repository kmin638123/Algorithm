import sys 
n, m = map(int, sys.stdin.readline().split())

powerList = []
nameList = []
for i in range(n):
    name, power = input().split()
    power = int(power)
    if powerList and powerList[-1] == power:  # 가장 처음 칭호만 저장해주기 위해
        continue
    powerList.append(power)
    nameList.append(name)

for _ in range(m):
    power = int(sys.stdin.readline())
    
    left, right = 0, len(powerList)-1
    answer = 0  
    while left<=right:
        mid = (left+right)//2
        if powerList[mid]<power:
            left = mid+1
        else:
            answer = mid
            right = mid-1
    print(nameList[answer])
    
####################################
from bisect import *
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[list(input().split()) for _ in range(n)] 
a,p=[i[0] for i in a],[int(i[1]) for i in a]
for _ in range(m): print(a[bisect_left(p,int(input()))])