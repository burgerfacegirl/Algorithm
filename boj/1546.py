n = int(input())
scores = list(map(int,input().split()))

max_num = max(scores)

sum_score = sum(scores)

print(sum_score)
new_average = (sum_score/max_num*100)/n

print(new_average)