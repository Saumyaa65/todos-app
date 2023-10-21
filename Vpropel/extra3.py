a=input()
b=input()
"""56
32"""
l=[]
s1=''
s2=''
n=min(len(a),len(b))
for i in range(n):
    s1=s1+a[i]+b[i]
    s2=s2+b[i]+a[i]
    a1=a[i+1:]
    b1=b[i+1:]
s1=s1+a1+b1
s2=s2+a1+b1
l.append(s1)
l.append(s2)

s1=''
s2=''
a1=str(max(int(a),int(b)))
b1=str(min(int(a),int(b)))

for i in range(n-1,-1,-1):
    c=len(a1)
    s1=s1+a1[c-1]+b1[i]
    s2=s2+b1[i]+a1[c-1]
    a1=a[:c-1]
    b1=b[:i]
s1=s1+a1+b1
s2=s2+a1+b1
l.append(s1)
l.append(s2)
print(l)
"""5362, 3526, 6253, 2635"""
print(max(l))
"""6253"""