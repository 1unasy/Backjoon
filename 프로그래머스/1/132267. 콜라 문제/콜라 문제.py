def solution(a, b, n):
    get_bottle = []
    while a <= n:
        get = (n // a) * b
        get_bottle.append(get)
        n = get + (n % a)
    return sum(get_bottle)