import sys
input = sys.stdin.readline

s = input().strip()

tag = []
check = 0
word = []

def words(word:list):
    reverse_word = []
    tmp = []
    # print(word)
    for i in word:
        if i==" ":
            tmp.reverse()
            reverse_word+=tmp
            reverse_word.append(i)
            tmp = []
        else:
            tmp.append(i)
    if tmp:
        tmp.reverse()
        reverse_word+=tmp
    return ''.join(reverse_word)

ans = ''
for i, value in enumerate(s):
    if not check:
        if value == "<":
            check = 1
            tag.append(value)
            ans+=words(word)
            word = []
        else:
            word.append(value)
    else:
        tag.append(value)
        if value == ">":
            check = 0
            ans += ''.join(tag)
            tag = []
            
ans+=words(word)
print(ans)