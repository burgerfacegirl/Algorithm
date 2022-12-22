# 221221_공던지기

def solution(numbers, k):
    n = len(numbers)-1
    t = 0
    c = 1       # 현재 공을 던지는 차례(번)

    if c == k:
        answer = numbers[0]
    else:
        while True:
            t += 2
            c += 1
            if t > n:
                if t == n+2:
                    t = 1
                elif t == n+1:
                    t = 0
            answer = numbers[t]
            if c == k:
                break


    return answer

print(solution([1, 2, 3, 4, 5, 6],5))