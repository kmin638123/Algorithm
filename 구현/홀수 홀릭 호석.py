num = input()

def cnt_odd(num):
    cnt = 0
    for m in num:
        if int(m) % 2 == 1: cnt+=1
    return cnt

def dfs(num, val):
    # print(num)
    # print(val)
    numbers = list(num)
    n = len(numbers)

    if n>2:
        for i in range(1, n-1):
            for j in range(i+1, n):
                new_num = int(("").join(numbers[:i]))+int(("").join(numbers[i:j]))+int(("").join(numbers[j:]))
                cnt = cnt_odd(list(str(new_num)))
                dfs(str(new_num), val+cnt)        
    elif n==2:
        num = str(int(num)//10+int(num)%10)
        dfs(num, val+cnt_odd(list(num))) 
    else:
        ans.add(val)
        return


val = cnt_odd(list(num))
ans = set()

dfs(num, val)
ans = sorted(list(ans))
print(ans[0], ans[-1])
        