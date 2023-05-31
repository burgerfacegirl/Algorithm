def solution(n):
    answer = 0

    N = len(str(n))
    t = 10 ** N

    for i in range(N):
        answer += n // t
        n = n % t
        if n // 10 == 0:
            answer += n % t
            break
        t = t // 10

    return answer