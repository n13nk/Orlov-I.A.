n = int(input())
a = [input().split() for i in range(n)]
for i in range(len(a)):
     for j in range(i , len(a)):
          a[i][j], a[j][i] = a[j][i], a[i][j]
for row in a:
     print(' '.join(row))