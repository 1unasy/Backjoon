n = int(input())
if not(1<=n<=9):
    print("n은 1~9 사이의 값을 입력해주세요.")
    n = int(input())
for x in range(1,10):
    print(f'{n} * {x} = {n*x}')