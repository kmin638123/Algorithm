import sys
from collections import Counter
input = sys.stdin.readline

word = input().rstrip().upper()

if len(word)==1:
    print(word)
else:
    alpha = Counter(word).most_common(2)
    if len(alpha)>1 and alpha[0][1]==alpha[1][1]:
        print("?")
    else:
        print(alpha[0][0])
#########################################################
# 시간복잡도 개선

import sys
x = sys.stdin.read()
x=x.upper()
arr = [0 for _ in range(91-65)]
for i in range(65,91):
    c=chr(i)
    count=x.count(c)
    arr[i-65]=count

M = max(arr)
if arr.count(M) > 1:
    print('?')
else:
    print(chr(arr.index(M)+65))