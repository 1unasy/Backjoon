a = int(input())
b = int(input())

splited_b = [int(x) for x in str(b)][::-1]
for x in splited_b:
    print(a * x, end='\n')
print(a*b)

# splited_b = [a * int(x) for x in str(b)][::-1]
# print(splited_b[0], splited_b[1], splited_b[2], sep='\n')
# print(a*b)
