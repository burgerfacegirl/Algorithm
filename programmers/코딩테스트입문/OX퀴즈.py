# 221212_코딩테스트 입문_OX 퀴즈_level 0

def solution(quiz):
    answer = []
    for equ in quiz:
        equs = equ.split(" ")
        if equs[1] == '+':
            ans = int(equs[0]) + int(equs[2])
        else:
            ans = int(equs[0]) - int(equs[2])

        if ans == int(equs[4]):
            answer.append("O")
        else:
            answer.append("X")

    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))