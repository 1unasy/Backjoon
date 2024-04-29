a, b = map(str, input().split())
su_a, su_b = int(a[::-1]), int(b[::-1])
print(su_a if su_a > su_b else su_b)