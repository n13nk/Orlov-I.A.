def j(n,d=2):
    if n==2 or d*d>n:
        return True
    if not (n%d):
        return False
    return j(n,d=d+1)
    
n = int(input("Введите число: "))
if j(n):
    print("YES")
else:
    print("NO ")