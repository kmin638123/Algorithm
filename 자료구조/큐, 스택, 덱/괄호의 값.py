import sys
s = sys.stdin.readline().rstrip()

nums = []
stk = []
check = 0

cnt1 = 0
cnt2 = 0

for i in s:
    if i == "(":
        stk.append("(")
        cnt1+=1
    elif i == "[":
        stk.append("[")
        cnt2+=1
    elif i ==")":
        if cnt1==0:
            check = 1
            break
        res = 0
        while True:
            if not stk:
                print(0)
                exit()
            i = stk[-1]
            if i == "(":
                if not res: res = 1
                stk.pop()
                stk.append(2*res)
                break
            elif i =="[":
                print(0)
                exit()
            else: # 숫자
                res+=stk[-1]
                stk.pop()
        cnt1-=1
    else:
        if cnt2==0:
            check = 1
            break
        res = 0
        while True:
            if not stk:
                print(0)
                exit()
            i = stk[-1]
            if i == "[":
                if not res: res = 1
                stk.pop()
                stk.append(3*res)
                break
            elif i =="(":
                print(0)
                exit()
            else: # 숫자
                res+=stk[-1]
                stk.pop()
        cnt2-=1
        
if check:
    print(0)
else:
    if cnt1:
        print(0)
    elif cnt2:
        print(0)
    else:
        print(sum(stk))
        
#######################################

# import sys
# s = sys.stdin.readline().rstrip()

# nums = []
# stk = []
# check = 0

# for i in s:
#     if i == "(":
#         stk.append("(")
#     elif i == "[":
#         stk.append("[")
#     elif i ==")":
        
#         res = 0
#         while True:
#             if not stk:
#                 print(0)
#                 exit()
#             i = stk[-1]
#             if i == "(":
#                 if not res: res = 1
#                 stk.pop()
#                 stk.append(2*res)
#                 break
#             elif stk and stk[-1] == '[': # 올바르지 않은 괄호
#                 print(0)
#                 exit()
#             else: # 숫자
#                 res+=stk[-1]
#                 stk.pop()
#     else:
#         res = 0
#         while True:
#             if not stk:
#                 print(0)
#                 exit()
#             i = stk[-1]
#             if i == "[":
#                 if not res: res = 1
#                 stk.pop()
#                 stk.append(3*res)
#                 break
#             elif stk and stk[-1] == '(': # 올바르지 않은 괄호
#                 print(0)
#                 exit()
#             else: # 숫자
#                 res+=stk[-1]
#                 stk.pop()
        
# for i in stk:
#     if i in ['(', ')', '[', ']']: 
#         print(0)
#         exit()
# else:
#     print(sum(stk))