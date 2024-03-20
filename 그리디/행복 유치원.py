import sys
input = sys.stdin.readline

n, k = map(int, input().split())
student = list(map(int, input().split()))

h = []

for i in range(1,n):
    h.append(student[i]-student[i-1])

h.sort(reverse=True)
print(sum(h[k-1:]))
