import sys
input = sys.stdin.readline

x, y = map(int, input().split())

def rev(num):
    rev_num = str(num)[::-1]
    return int(rev_num)

print(rev(rev(x)+rev(y)))