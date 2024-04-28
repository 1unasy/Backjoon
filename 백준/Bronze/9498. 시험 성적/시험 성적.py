score = int(input())
# 0 ~ 100 사이 아닐 경우 다시 입력
if not (0<= score <= 100):
    print('score는 0~100 사이의 숫자를 입력해주세요.')
    score = int(input())
# 점수별 성적 부여
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')