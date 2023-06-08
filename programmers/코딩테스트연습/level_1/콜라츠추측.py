def solution(num):
    answer = 0
    cnt = 0

    if num != 1:
        while num != 1 and cnt < 500:
            if num % 2:
                num = num * 3 + 1
                cnt += 1
            else:
                num = num // 2
                cnt += 1

    if num == 1:
        answer = cnt
    else:
        answer = -1

    return answer