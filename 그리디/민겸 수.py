# 내 풀이
s = input()

max_value = ""
min_value = ""

tmp = 0
for i in s:
    if i == "K":
        max_value+=str(5*(10**tmp))
        if tmp == 0: 
            min_value += "5"
        else:
            min_value+=(str(10 ** (tmp-1))+"5")
        tmp = 0
    else:
        tmp+=1

if tmp!=0:
    max_value += "1" *tmp
    min_value += str(10 ** (tmp-1))
    
print(int(max_value))
print(int(min_value))
