n = int(input())
score = list(map(int, input().split()))
max_score = max(score)

modified_score = [i/max_score*100 for i in score]
print(sum(modified_score)/n)