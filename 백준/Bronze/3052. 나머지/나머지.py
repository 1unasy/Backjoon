lefts = []
for _ in range(10):
    n = int(input())
    left = n % 42
    lefts.append(left)

print(len(set(lefts)))