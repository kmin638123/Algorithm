import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    word = input().rstrip()
    check = 0 
    for i in range(len(word)):
        alpha = word[i]
        if alpha in word[i+1:]:
            if word[i+1]!=alpha:
                check = 1
                continue
    
    if not check:
        cnt+=1
        
print(cnt)