def solution(t, p):
    result = [t[i:i+len(p)] for i in range(len(t)-len(p)+1)]
    return len([x for x in result if int(x) <= int(p)])