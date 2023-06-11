def solution(operations):
    q = []
    for quiz in operations:
        quiz_l = quiz.split(" ")
        if quiz_l[0] == 'I':
            q.append(int(quiz_l[1]))
        elif quiz_l[0] == 'D':
            if q:
                if int(quiz_l[1]) == 1:
                    q.remove(max(q))
                else:
                    q.remove(min(q))
    if q:
        answer = [max(q), min(q)]
    else:
        answer = [0, 0]
    return answer