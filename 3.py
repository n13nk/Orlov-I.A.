n=int(input())
m=n
h=m//60
m=n%60
if n<1440:
    print(h,m,sep=':')
else:
    d=h//24
    h%=24
    print(d,'days',h,':',m)