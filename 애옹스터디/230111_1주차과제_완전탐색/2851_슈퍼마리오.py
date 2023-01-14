# boj_2851_슈퍼마리오_완전탐색

mushrooms = list(int(input()) for _ in range(10))
score = 0
ans = 0

for i in range(0, 10):
    score += mushrooms[i]
    if score >= 100:
        if abs(score-100) <= abs(score-mushrooms[i]-100):
            ans = score
        else:
            ans = score-mushrooms[i]
        break
    elif i == 9 and score < 100:
        ans = score
        break

print(ans)

