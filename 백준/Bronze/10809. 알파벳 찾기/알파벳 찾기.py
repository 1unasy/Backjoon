word = input()
aList = [chr(i) for i in range(ord('a'),ord('z')+1)]
for alpha in aList:
    if alpha in word:
        print(word.index(alpha), end=' ')
    else:
        print(-1, end=' ')