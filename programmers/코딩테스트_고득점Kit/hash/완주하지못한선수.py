# 221214_완주하지 못한 선수_level_1

def solution(participant, completion):
    answer = ''
    parti = {}
    comple = {}
    for par in participant:
        if par in parti.keys():
            parti[par] += 1
        else:
            parti[par] = 1

    for com in completion:
        if com in comple.keys():
            comple[com] += 1
        else:
            comple[com] = 1

    for par in participant:
        if (par not in comple.keys()) or (parti[par] != comple[par]):
            answer = par

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))