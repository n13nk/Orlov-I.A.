a=int(input())
b=int(input())
def F(a,b):
    if a<b:
        for i in range(a,b+1,+1):
            print(i,end=" ")
    else:
        for i in range(a,b-1,-1):
            print(i,end=" ")
F(a,b)