def solution(d, budget):
    d.sort()
    n = len(d)
    answer = 0

    for i in range(n):
        if budget - d[i] >= 0:
            answer += 1
            budget -= d[i]
        else:
            break

    return answer