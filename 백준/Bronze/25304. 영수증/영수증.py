total = int(input())
goods = int(input())
sum = 0

for _ in range(goods):
    price, nums = map(int, input().split())
    sum += price * nums

print('Yes' if total == sum else 'No')