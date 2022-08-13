# OX 퀴즈 - 브론즈 2
# 알고 스터디 8/11 문제

T = int(input())

for tc in range(1, T+1):
    S = input()
    total = score = 0

    for i in S:
        if i == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)
