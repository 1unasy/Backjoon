n = int(input())
score = list(map(int, input().split()))

modified_score = [i/max(score)*100 for i in score]
print(sum(modified_score)/n)