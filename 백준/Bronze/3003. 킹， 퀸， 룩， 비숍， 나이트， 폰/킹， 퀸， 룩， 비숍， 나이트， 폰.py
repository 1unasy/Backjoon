now_chess = list(map(int,input().split()))
original = [1, 1, 2, 2, 2, 8]

for n, o in zip(now_chess, original):
    print(o-n, end=' ')