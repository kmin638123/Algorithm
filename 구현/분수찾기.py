# 시간 초과 풀이
# X = int(input())
    
# dir = [[0,1], [1,0]] # 아래, 오른쪽으로 이동 (방향 전환)
# go = [[1,-1], [-1,1]] # 왼쪽 아래, 오른쪽 위로 이동 

# n = 0
# x, y = 0,0
# cnt = 1 # 1 포함

# dir_idx = go_idx = 0

# def check(x,y):
#     global cnt
#     if cnt == X:
#         print(str(x+1)+"/"+str(y+1))
#         exit()
# if X==1:
#     check(x,y)
       
# while True:
    
#     x+=dir[dir_idx][0]
#     y+=dir[dir_idx][1]
#     cnt+=1
#     check(x,y) 
    
#     n+=1   
    
#     for i in range(n):

#         x+=go[go_idx][0]
#         y+=go[go_idx][1]
#         cnt+=1
#         check(x,y)
    
#     dir_idx = 1 - dir_idx
#     go_idx = 1 - go_idx

#################################################
x = int(input())
line = 1 # 몇번째 줄인지
idx = 0 # 해당 줄에 몇 번째 분수인지

while x>line:
    x -= line
    line+=1
idx = x

a,b = 0,0 # 분자, 분모

if line % 2 == 1: # 홀수번째 줄이면, 분자 감소/분모 증가
    a = line-(x-1)
    b = x
else:
    a = x
    b = line-(x-1)
    
print(str(a)+"/"+str(b))