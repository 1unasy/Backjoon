a = int(input())
b = int(input())

splited_b = [int(x) for x in str(b)][::-1]
for x in splited_b:
    print(a * x, end='\n')
print(a*b)
