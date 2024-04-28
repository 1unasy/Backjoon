x = int(input())
y = int(input())
if not(-1000<=x<=1000) and not(-1000<=y<=1000):
    print('x, y는 -1000~1000 사이의 숫자를 입력해주세요.')
    x = int(input())
    y = int(input())
if x > 0:
    print('1' if y > 0 else '4')
else:
    print('2' if y > 0 else '3')