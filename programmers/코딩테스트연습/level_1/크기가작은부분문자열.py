def solution(t, p):
    n = len(t)
    m = len(p)

    answer = 0

    for i in range(n - m + 1):
        if int(t[i:i + m]) <= int(p):
            answer += 1

    return answer