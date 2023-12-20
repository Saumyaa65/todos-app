t=int(input())
for z in range(t):
    l=input().split()
    n=int(l[0])
    p=int(l[1])
    l=[]
    for i in range(n):
        l.append(0)
    ch=0
    while(p>0):
        for i in range(ch,n):
            c=l[i]
            l[i]=c+1
            p=p-1
        if ch==n:
            c=l[0]
            l[0]=c+p
            break
        ch=ch+1
    print(l)
