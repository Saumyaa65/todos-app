t=int(input())
for p in range(t):
    l=input().split()
    row=int(l[0])
    col=int(l[1])
    l=[]
    ip=input().split()
    c=0
    for i in range(row):
        k=[]
        for j in range(col):
            k.append(int(ip[c]))
            c+=1
        l.append(k)
    gen=[]
    c=0
    for i in range(row-1,-1,-2):
        if(c<col):
            n=l[i][c]
            gen.append(n)
            c+=1
    for i in range(2,row,2):
        if(c<col):
            n=l[i][c]
            gen.append(n)
            c+=1

    pw=''
    for i in gen:
        if i>26:
            while(i>26):
                i=i-26
        ch = chr(i + 96)
        pw=pw+ch

    print(pw)