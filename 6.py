def dots(x,y,x1,y1):
    if (x+y+x1+y1)%2==0:
        print('Yes')
    else:
        print('No')
dots(int(input()),int(input()),int(input()),int(input()))