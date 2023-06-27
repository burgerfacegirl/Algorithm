def solution(n):
    three = ''
    while n > 0:
        three += str(n % 3)
        n = n // 3

    three = three[::-1]

    answer = 0
    n = len(three)
    for i in range(n):
        answer += int(three[i]) * (3 ** i)
    return answer