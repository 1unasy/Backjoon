while True:
    try:
        print(input())
    except EOFError:
        break

# 성능은 동일하게 48ms, 입력값 없을 때도 중지되도록 함
#while True:
#    try:
#        word = input()
#        if word != '':
#            print(word)
#        else:
#            break
#    except EOFError:
#        break
