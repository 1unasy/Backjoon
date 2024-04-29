n = int(input())
number = input()
if n != len(number):
    print(f'{n}개의 숫자를 공백없이 입력해주세요.')
    number = int(input())
else:
    sum = 0
    for num in number:
        sum += int(num)
    print(sum)