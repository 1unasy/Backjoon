n = int(input())
print('\n'.join([' '*(n-i)+'*'*i for i in range(1,n+1)]))