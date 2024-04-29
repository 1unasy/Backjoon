word = input().lower()
dict = {}
for w in list(set(word)):
    dict[w] = word.lower().count(w)

if list(dict.values()).count(max(dict.values())) > 1:
    print('?')
else:
    print(max(dict, key=dict.get).upper())