n=int(input())
a=1
b=0
s=0
for i in range(1,n+1):
    c=a
    a=c+b
    b=c
    s+=c
print(s)