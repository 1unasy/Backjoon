h, m = map(int, input().split())
if not(0<=h<=23) and not(0<=m<=59):
    print('0<=h<=23, 0<=m<=59에 해당하는 값을 입력해주세요.')
    h = int(input())
    m = int(input())
if m < 45:
    if h == 0:
        h = 23
        m += 60
    else:
        h -= 1
        m += 60
print(h, m-45)