def solution(price, money, count):
    p = 0
    for i in range(1, count+1):
        p += price * i
    answer = p - money if p >= money else 0

    return answer