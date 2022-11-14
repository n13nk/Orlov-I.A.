def c(n,m,k):
    if (k%n==0 or k%m==0) and (k<n*m):
        print('Yes')
    else:
        print('No')
c(int(input()),int(input()),int(input()))