p=1
s=0
A=[int(i) for i in input().split()]
for a in A:
    s+=a
    p*=a
print('Сумма элементов равна',s)
print('Произведение элементов равно',p)