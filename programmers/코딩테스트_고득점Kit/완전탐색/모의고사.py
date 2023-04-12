def solution(answers):
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    person = [0] * 4
    answer = []
    for i in range(len(answers)):
        if answers[i] == m1[i % 5]:
            person[1] += 1
        if answers[i] == m2[i % 8]:
            person[2] += 1
        if answers[i] == m3[i % 10]:
            person[3] += 1

    best = max(person)
    for i in range(1, 4):
        if person[i] == best:
            answer.append(i)

    return answer