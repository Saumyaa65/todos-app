from itertools import combinations as cb
t=int(input())
for z in range(t):
    l=input().split()
    r=int(l[0])
    n=int(l[1])
    p=n
    x=n//r
    rem=n%r
    l=[]
    for i in range(r):
        l.append(x)
        n=n-x
    for i in range(r):
        if n==0:
            break
        c=l[i]
        l[i]=c+1
        n=n-1
    print(l)
    n=p
    l1=[]
    l1=list(cb(range(1,n+1),l[0]))
    print(l1)
    print(len(l1))
