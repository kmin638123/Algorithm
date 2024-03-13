# 시간초과 => 큐로 구현해야 한다.
# n = int(input())

# cards = [i+1 for i in range(n)]

# while len(cards)>1:
#     cards.pop(0)
#     top=cards.pop(0)
#     cards.append(top)
    
# print(cards[0])
###################################'
from collections import deque
n = int(input())

cards = [i+1 for i in range(n)]
queue = deque(cards)

while len(queue)>1:
    queue.popleft()
    top=queue.popleft()
    queue.append(top)
    
print(queue[0])