h, m = map(int, input().split())
cook_time = int(input())

af_m = m + cook_time
af_h = h + (af_m//60)
af_m = af_m - (60*(af_m//60)) if af_m % 60 else 0

print(af_h if af_h < 24 else af_h-24, af_m)