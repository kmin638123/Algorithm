# 내 풀이
n = int(input())

if (n%5)%2==0:
    print(n//5 + (n-(n//5)*5)//2) 
else:
    five = n//5 - 1
    answer = -1 if five == -1 else five + (n-five*5)//2
    print(answer)

####################################   
# 그리디 
n = int(input())

cnt = 0

# 처음 입력 받은 금액을 0이나 음수가 될 때까지
# 무한 반복문을 사용해 5로 나누어 떨어질 때까지 2를 빼면 된다.

while n > 0:
    if n % 5 == 0:
        cnt += n//5
        break
    else:
        n -= 2
        cnt+=1
if n < 0:
    print(-1)
else:
    print(cnt)
        