import sys
from collections import Counter
from itertools import combinations

input = sys.stdin.readline
t = Counter(input().rstrip())
n = int(input())

books = []

for _ in range(n):
    price, title = input().split()
    books.append([Counter(title), int(price)])

def check(comb):
    tmp = t
    p = 0
    for book in comb:
        tmp = tmp - book[0]
        p+=book[1]
    
    if not tmp:
        return p
    else: return 0

ans = 1e9

for i in range(1,n+1):
    b = combinations(books,i)

    for book in b:
        res = check(list(book))
        if res:
            ans = min(ans,res)

if ans == 1e9:
    ans = -1
  
print(ans)
        
