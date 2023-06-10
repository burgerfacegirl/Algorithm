def solution(seoul):
    answer = ''
    for idx, word in enumerate(seoul):
        if word == "Kim":
            answer = '김서방은 ' + str(idx) + '에 있다'
    return answer