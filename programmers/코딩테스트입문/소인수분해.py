def solution(n):
    answer = []

    k = n
    for i in range(2, k + 1):
        while n % i == 0:
            answer.append(i)
            n = n // i
        if n < i :
            break

    answer = sorted(list(set(answer)))

    return answer

