n = int(input())
i = 0
for x in range(n*2-1):
    if x < n:
        i += 1
    else: i -= 1
    print(' '* (n-i) + '*' * (i * 2 - 1))