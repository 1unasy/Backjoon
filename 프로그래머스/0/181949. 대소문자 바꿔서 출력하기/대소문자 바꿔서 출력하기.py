str = input()
answer = [i.lower() if i.isupper() else i.upper() for i in str]
print(''.join(answer))
