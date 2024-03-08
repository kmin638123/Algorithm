from bisect import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

for _ in range(m):
    start, end = map(int, input().split())
    print(bisect_right(points, end)-bisect_left(points, start))