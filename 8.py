s=input('Введите строку, с точкой в конце: ')
p=' '
t='.'
k=0
for i in s:
    if i!=p and i!=t:
        k=k
    elif i==p:
        k=k+1
    if i==t:
        k=k+1
print('Количество слов в введённой строке: ', k)