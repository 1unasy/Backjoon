n, m = map(int, input().split())
basket = [0 for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a,b+1):
        basket[i] = c

for i in basket[1:]:
    print(i, end=' ')