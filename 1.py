def num_num(n):
    i = n
    while (i >= 0):
        remainder = i % 10
        if (remainder!=0):
            c = (n / remainder) * 10000
        else:
            c=1
        if (c % 10000 == 0):
            print (remainder)
        i = i // 10
    return 0
    
print(num_num(1244352243))