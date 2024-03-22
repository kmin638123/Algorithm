c_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]

s = input().rstrip()

for i in c_alpha:
    s=s.replace(i,"a")
print(len(s))