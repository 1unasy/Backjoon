one, two, three = map(int, input().split())

# 주사위 눈 3개 동일
if one == two and two == three:
    print(10000+one*1000)
# 주사위 눈 2개 동일
elif one == two or one == three or two == three:
    print(1000+two*100 if two == three else 1000+one*100)
# 주사위 눈 동일 X
else:
    print(max(one, two, three)*100)