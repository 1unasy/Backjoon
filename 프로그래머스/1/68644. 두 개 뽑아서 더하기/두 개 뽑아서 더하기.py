from itertools import combinations 

def solution(numbers):
    return sorted(set([x+y for x,y in list(combinations(numbers,2))]))