# 메모리 초과 풀이
        
# from collections import deque

# s = int(input())


# queue = deque()
# queue.append((1,0,0)) # 화면, 클립보드의 각 이모티콘 개수, + 시간

# while queue:
#     screen, clipboard, time= queue.popleft()
#     if screen == s:
#         print(time)
#         break   
    
#     # 클립보드에 저장
#     new_clipboard = screen
#     queue.append((screen, new_clipboard, time+1))
    
#     # 붙여넣기
#     if clipboard:
#         new_screen = screen+clipboard
#         queue.append((new_screen, clipboard, time+1))
        
#     # 삭제
#     if screen:
#         new_screen = screen -1
#         queue.append((new_screen, clipboard, time+1))
##############################################
#  visited 추가!
from collections import deque

s = int(input())


queue = deque()
queue.append((1,0,0)) # 화면, 클립보드의 각 이모티콘 개수, + 시간

visited = [[False] * 1001 for _ in range(1001)]
visited[1][0] = True

while queue:
    screen, clipboard, time= queue.popleft()
    if screen == s:
        print(time)
        break   
    
    for i in range(3):
        new_screen, new_clipboard = screen, clipboard
        if i==0: # 클립보드에 저장
            new_clipboard = screen
        elif i ==1: # 붙여 넣기
            if clipboard:
                new_screen = screen+clipboard
        else: #삭제
            if screen:
                new_screen = screen -1

        if 0<=new_clipboard<=1000 and 0<=new_screen<=1000 and not visited[new_screen][new_clipboard]:
            queue.append((new_screen, new_clipboard, time+1))
            visited[new_screen][new_clipboard] =True