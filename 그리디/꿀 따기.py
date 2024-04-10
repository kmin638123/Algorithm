# import sys
# input = sys.stdin.readline

# n = int(input())
# honey = list(map(int, input().split()))

# tot = sum(honey)
# ans = 0

# # 벌 벌 꿀
# bee1 = tot-honey[0]
# bee2 = 0

# # 벌 꿀 벌
# h = 0

# # 꿀 벌 벌
# bee3 = tot - honey[-1]
# bee4 = 0

# for i in range(1, n-1):
#     bee2 = max(bee2, sum(honey[i:])-honey[i]*2)
#     h = max(h, honey[i])
#     bee4 = max(bee4, sum(honey[:n-i])-honey[n-i-1]*2)

# # print(bee1+bee2)
# # print(tot+h-honey[0]-honey[-1])
# # print(bee3+bee4)


# ans = max(bee1+bee2, tot+h-honey[0]-honey[-1], bee3+bee4)
# print(ans)
##################################################
#
import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))

# 누적합!! 을 이용해보자 ~
prefix_sum = [honey[0]]
for i in range(1, n):
    prefix_sum.append(prefix_sum[-1]+honey[i])
    
# 벌 벌 꿀
bee1 = prefix_sum[-1]-honey[0]

# 꿀 벌 벌
bee3 = prefix_sum[n-2]

bee2, h, bee4 = 0, 0, 0
for i in range(1,n-1):
    bee2= max(bee2, prefix_sum[-1]-prefix_sum[i]-honey[i])
    bee4 = max(bee4, prefix_sum[i-1]-honey[i])
    h = max(h, honey[i])
    
print(max(bee3+bee4, bee1+bee2, prefix_sum[n-2]-honey[0]+h))