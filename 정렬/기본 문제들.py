# 대표값
import sys
from collections import Counter
numbers = [int(sys.stdin.readline().rstrip()) for _  in range(10)]

print(sum(numbers)//10)
print(Counter(numbers).most_common(1)[0][0])
###############################################
# 대표값2
import sys
numbers = [int(sys.stdin.readline().rstrip()) for _  in range(5)]

print(sum(numbers)//5)
print(sorted(numbers)[2])

###########################################  
# 커트라인
import sys
n, k = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))

print(sorted(nums, reverse=True)[:k][-1])

###########################################  
#소트인사이드
nums = list(map(lambda x: int(x),list(input())))
for num in sorted(nums, reverse=True):
    print(num, end="")

###########################################  
# 좌표 정렬하기
import sys

n = int(input())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for a, b in sorted(points, key=lambda x: (x[0],x[1])):
    print(str(a)+" "+str(b))

###########################################  
# 좌표 정렬하기 2
import sys

n = int(input())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for a, b in sorted(points, key=lambda x: (x[1],x[0])):
    print(str(a)+" "+str(b))

###########################################  
# 단어 정렬
import sys 

n = int(input())
words = list(set([sys.stdin.readline().rstrip() for _ in range(n)]))

for word in sorted(words, key = lambda x: (len(x),x)):
    print(word)

###########################################  
# 나이순 정렬
import sys 

n = int(input())
members = []
for i in range(n):
    a, b = sys.stdin.readline().split()
    members.append([int(a),b,i])
    
for age, name, idx in sorted(members, key=lambda x:(x[0],x[2])):
    print(str(age)+" "+name)

###########################################  
# 좌표 압축
# 시간 초과 풀이
# list.index(i)는 O(N)의 시간복잡도
# import sys 

# n = int(input())
# nums = list(map(int, sys.stdin.readline().split()))
# sorted_num = sorted(nums)
# for num in nums:
#     print(sorted_num.index(num), end =" ")

# => dict[i]의 형태로 시간복잡도 O(1)로 해결해야 함
import sys 

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
sorted_num = sorted(list(set(nums)))

dic = {sorted_num[i]:i for i in range(len(sorted_num))}

for num in nums:
    print(dic.get(num), end =" ")

###########################################  
# 통계학
import sys
from collections import Counter

n = int(input())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
nums.sort()

print(round(sum(nums)/len(nums)))
print(nums[(len(nums)-1)//2])
count = list(Counter(nums).most_common(2))

most = count[0][0]
if len(count)>1 and count[0][1]==count[1][1]:
    most = count[1][0] 

print(most)
print(nums[-1]-nums[0])