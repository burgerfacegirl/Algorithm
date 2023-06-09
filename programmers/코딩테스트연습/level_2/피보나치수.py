
def solution(n):
    if n == 0:
        answer = 1234567
    elif n == 1:
        answer = 1234567
    else:
        fibo_list = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2]

        answer = fibo_list[n] % 1234567

    return answer