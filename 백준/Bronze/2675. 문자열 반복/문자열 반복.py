num = int(input())
for _ in range(num):
    repeat, wrd = map(str,input().split())
    for i in wrd:
        print(i*int(repeat), end='')
    print()