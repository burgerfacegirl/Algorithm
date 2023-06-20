def solution(people, limit):
    answer = 0

    people.sort()
    n = len(people)
    check = [0] * n

    i = 0
    j = n - 1

    while i < j:
        if people[i] + people[j] == limit:
            answer += 1
            check[i] = 1
            check[j] = 1
            i += 1
            j -= 1
        elif people[i] + people[j] > limit:
            j -= 1
        else:
            answer += 1
            check[i] = 1
            check[j] = 1
            i += 1
            j -= 1

    answer += check.count(0)

    return answer