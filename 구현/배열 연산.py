# 정사각형 회전 하기
square = [[1,2,3],[4,5,6],[7,8,9]]
n = len(square)

# 시계 방향 90도 회전
rotated_90 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated_90[j][n-i-1] = square[i][j]
print(rotated_90)     
 
# 시계 방향 180도 회전
rotated_180 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated_180[n-i-1][n-j-1] = square[i][j]
print(rotated_180)     

# 시계 방향 270도 회전
rotated_270 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated_270[n-j-1][i] = square[i][j]
print(rotated_270)         

################################################################
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # 3x4 배열 

# 2차원 배열 행열 바꾸기
print(list(zip(*arr)))

n, m = len(arr), len(arr[0])
# 직사각형 시계방향 90도 회전
rotated_90 = [[0] * n for _ in range(m)]
for i in range(n):
    for j in range(m):
        rotated_90[j][n-i-1] = arr[i][j]
print(rotated_90)

# 직사각형 시계방향 180도 회전
rotated_180 = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        rotated_180[n-i-1][m-j-1] = arr[i][j]
print(rotated_180)  

# 직사각형 시계방향 270도 회전
rotated_270 =[[0] * n for _ in range(m)]
for i in range(n):
    for j in range(m):
        rotated_270[m-j-1][i] = arr[i][j]
print(rotated_270)        
