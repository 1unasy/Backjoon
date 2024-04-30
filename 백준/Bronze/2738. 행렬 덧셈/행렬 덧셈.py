n, m = map(int, input().split())
matrix1, matrix2 = [], []
for i in range(n*2):
    row = list(map(int, input().split()))
    if len(row) != m:
        print(f'{m}개의 숫자를 한 줄로 입력해주세요.(구분자=공백)')
        row = list(map(int, input().split()))
    if i < n*2//2:
        matrix1.append(row)
    else:
        matrix2.append(row)

for row in range(n):
    for col in range(m):
        print(matrix1[row][col]+matrix2[row][col], end=' ')
    print()