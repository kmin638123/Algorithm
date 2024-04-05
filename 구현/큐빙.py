import sys
from copy import deepcopy
input = sys.stdin.readline

def rot(d, v):
    new = [[0] * 3 for _ in range(3)]
    if v=="+":
        for i in range(3):
            for j in range(3):
                new[j][3-i-1] = cube[d][i][j]
    else:
        for i in range(3):
            for j in range(3):
                new[3-j-1][i] = cube[d][i][j]
                        
    return new

def fb(v):
    u, d,l,r = deepcopy(cube[0]), deepcopy(cube[1]),deepcopy(cube[4]),deepcopy(cube[5])
    if v==0: #f
        cube[2]=rot(2,"+")
        for j in range(3):
            cube[0][2][j] = l[2-j][2]
            cube[1][2][j] = r[2-j][0]
            cube[4][j][2] = d[2][j]
            cube[5][j][0] = u[2][j]
    else: # b
        cube[3]=rot(3,"+")
        for j in range(3):
            cube[5][j][2] = d[0][j]
            cube[4][j][0] = u[0][j]
            cube[0][0][j] = r[j][2]
            cube[1][0][j] = l[j][0]
                    
    return cube              

t = int(input())
for _ in range(t):
    n = int(input())
    cube = [[["w"]*3 for _ in range(3)], [["y"]*3 for _ in range(3)], [["r"]*3 for _ in range(3)],[["o"]*3 for _ in range(3)],[["g"]*3 for _ in range(3)],[["b"]*3 for _ in range(3)]]
    cubing = input().split()
    # print(cubing)
    for c in cubing:
        # print(cube)
        if c[0]=="U" or c[0]=="D":
            if c[0]=="U":
                line = 0
                cube[0]=rot(0,c[1])
            else:
                line = 2
                cube[1]=rot(1,c[1])
                
            f,b,l,r=cube[2][line],cube[3][line],cube[4][line],cube[5][line]
            
            if c=="U-" or c=="D+":
                r.reverse()
                b.reverse()
                cube[2][line],cube[3][line],cube[4][line],cube[5][line]=l,r,b,f
            else:
                l.reverse()
                f.reverse()
                cube[2][line],cube[3][line],cube[4][line],cube[5][line]=r,l,f,b

        elif c[0]=="L" or c[0]=="R":
            if c[0]=="L":
                line = 0
                cube[4] = rot(4, c[1])
            else:
                line = 2
                cube[5] = rot(5, c[1])
            
            tmp = []
            for i in range(4):
                tmp.append([cube[i][j][line] for j in range(3)])
            u,d,f,b=tmp[0],tmp[1],tmp[2],tmp[3]
            
            if c=="L-" or c=="R+":
                idx = [2,3,1,0]
                for i in range(4):
                    if 0<=i<=1:
                        for j in range(3):
                            cube[i][j][line] = tmp[idx[i]][j]
                    else:
                        for j in range(3):
                            cube[i][j][line] = tmp[idx[i]][2-j]
            else:
                idx = [3,2,0,1]
                for i in range(4):
                    if 2<=i<=3:
                        for j in range(3):
                            cube[i][j][line] = tmp[idx[i]][j]
                    else:
                        for j in range(3):
                            cube[i][j][line] = tmp[idx[i]][2-j]        
        
        else: #F, B
            version = 0 if c[0]=="F" else 1
            if c[1]=="+":
                cube = fb(version)
            else:
                for _ in range(3):
                    cube = fb(version)
                
    for line in cube[0]:
        print(*line, sep="")
    # print(cube[0])