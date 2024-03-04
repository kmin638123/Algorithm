# 내 풀이
board = input()

p = ''
tmp = 0
answer = 0
for i in board:
    if i==".":
        if tmp%2==1:
            tmp = -1
            break
        p+='AAAA'*(tmp//4)
        p+='BB'*((tmp-(tmp//4)*4)//2)
        p+='.'
        tmp = 0
    else: 
        tmp += 1

if tmp == -1 or tmp%2==1:
    p = -1
elif tmp !=0:
    p+='AAAA'*(tmp//4)
    p+='BB'*((tmp-(tmp//4)*4)//2)

print(p)
###########################
# replace 이용해서 AAAA => BB 순서로 바꿔줌 

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)
