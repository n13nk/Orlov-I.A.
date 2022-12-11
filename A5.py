n = int(input(" Введите число N = "))
def q(n):        
    if  n:
        print(n%10,end=' ')
        q(n//10)
q(n)