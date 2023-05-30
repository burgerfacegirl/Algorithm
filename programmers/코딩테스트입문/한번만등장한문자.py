def solution(s):
    answer = ''

    for ss in s:
        if s.count(ss) == 1:
            answer += ss

    return "".join(sorted(answer))