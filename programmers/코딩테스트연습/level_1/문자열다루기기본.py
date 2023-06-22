def solution(s):
    answer = True
    n = len(s)
    if n != 4 and n != 6:
        answer = False

    for ss in s:
        if ss.isalpha():
            answer = False
    return answer