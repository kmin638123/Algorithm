# reverse 를 쓰면 시간초과가 뜨는 듯
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    
    if n==0:
        arr = input().rstrip()
        if "D" in p:
            print("error")
        else:
            print(arr)  
        continue
        
    arr = deque(list(map(int, input().rstrip()[1:-1].split(","))))
    check = 0
    dir = 0
    for i in p:
        if i =="R":
            dir = 1-dir
            # arr.reverse()
        else:
            if len(arr) == 0:
                check = 1
                break
            if not dir:
                arr.popleft()
            else:
                arr.pop()
    if check:
        print("error")
    else:
        if dir == 1:
            arr.reverse()
        print(str(list(arr)).replace(" ",""))
        