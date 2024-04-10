import sys
input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()

sl = len(s)

def dfs(t):
    global sl
    if t==s:
        print(1)
        exit()
    if len(t)==sl:
        return 0

    if t[-1]=="A":
        dfs(t[:-1])
    if t[0] =="B":
        dfs(t[1:][::-1])
    return 0

print(dfs(t))