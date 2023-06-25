def solution(n, m):
    a = max(n, m)
    check = [0] * (a + 1)

    answer = []

    def check_division(n):
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if i != n ** 0.5:
                    check[i] += 1
                    check[n // i] += 1
                else:
                    check[i] += 1

    check_division(n)
    check_division(m)

    for i in range(len(check) - 1, -1, -1):
        if check[i] == 2:
            answer.append(i)
            answer.append(n * m // i)
            break

    return answer