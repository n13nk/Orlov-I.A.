a = [[1,2,3,4,5,6],
     [1,2,3,4,5,6],
     [1,2,3,4,5,6],
     [1,2,3,4,5,6],
     [1,2,3,4,5,6],
     [1,2,3,4,5,6]]
k = 3
for i in a:
    print(*i,sep='\t')
for j in range(len(a)):
    a[k][j]=(a[k][j]/a[k][k])
print()
for i in a:
    print(*i,sep='\t')