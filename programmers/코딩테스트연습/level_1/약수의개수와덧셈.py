def solution(left, right):
    def divisor(n):
        div = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if n // i != i:
                    div.append(i)
                    div.append(n // i)
                else:
                    div.append(i)
        return len(div)

    answer = 0

    for i in range(left, right + 1):
        cnt = divisor(i)
        if cnt % 2:
            answer -= i
        else:
            answer += i

    return answer