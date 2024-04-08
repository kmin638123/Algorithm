import sys
input = sys.stdin.readline

name = input().rstrip()
n = int(input())
team = [input().rstrip() for _ in range(n)]
arr = []

for i in range(n):
    t = name+team[i]
    L, O, V, E = t.count("L"),t.count("O"),t.count("V"),t.count("E")
    res = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    
    arr.append((team[i], res))

print(sorted(arr, key=lambda x: (-x[1],x[0]))[0][0])