inp = input()
phone_dial = {('A','B','C'):2, ('D','E','F'):3, ('G','H','I'):4, ('J','K','L'):5, ('M','N','O'):6, ('P','Q','R','S'):7, ('T','U','V'):8, ('W','X','Y','Z'):9}
time = 0
for word in inp:
    for key, value in phone_dial.items():
        if word in key:
            time += 2+1*(value-1)
print(time)