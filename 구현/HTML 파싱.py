import sys
input = sys.stdin.readline

html = input().strip()
html.replace("</main>","")

def tag(p):
    idx = []
    for i, value in enumerate(p):
        if value=="<":
            idx.append([i])
        elif value == ">":
            if len(idx)==0:
                continue
            idx[-1].append(i)
    # print(idx)
    p = list(p)        
    for start, end in idx:
        for i in range(start, end+1):
            p[i]=">"
    p = ''.join(p)
    return p.replace(">","")


for s in html.split("</div>"):
    for i, div in enumerate(s.split('"')):
        if i == 1:
            print("title : " + div)
        elif i ==2:
            for p in div.split("</p>"):
                if p=="":
                    continue
                # for i in tag:
                #     p= p.replace(i,"")
                p =tag(p)
                p.strip()
                while "  " in p:
                    p = p.replace("  "," ")
                print(p)

