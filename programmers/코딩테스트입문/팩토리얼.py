# 221222_팩토리얼

def solution(n):
    def facto(n):
        if n == 1:
            return n
        else:
            return n * facto(n - 1)
    factos = [facto(1), facto(2)]
    for i in range(2, 10):
        factos.append(factos[i-1] * (i+1))

    for i in range(9, -1, -1):
        if n >= factos[i]:
            answer = i+1
            break
    return answer



print(solution(10))