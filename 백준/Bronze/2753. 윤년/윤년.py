year = int(input())
# 연도는 1 ~ 4000
if not(1<= year <=4000):
    print('연도는 1~4000 사이의 숫자를 입력해주세요.')
    year = int(input())
if ((year%4==0) and (year%100)) or (year%400==0):
    print('1')
else:
    print('0')