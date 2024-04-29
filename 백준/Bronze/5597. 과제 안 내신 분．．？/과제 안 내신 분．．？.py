students = [i for i in range(1,31)]
submitted = []
for _ in range(28):
    n = int(input())
    submitted.append(n)

diff = set(students) - set(submitted)

for i in sorted(diff):
    print(i)