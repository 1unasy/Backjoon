n = int(input())
num = list(map(int, input().split()))
if n != len(num):
    compared = '적습니다' if len(num) < n else '많습니다'
    print(f'입력 숫자 개수가 {n}개 보다 {compared}. 다시 입력해주세요.')
    num = list(map(int, input().split()))
find = int(input())
print(num.count(find))