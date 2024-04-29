n, m = map(int, input().split())
basket = [0 for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a-1,b):
        basket[i] = c

for i in basket:
    print(i, end=' ')