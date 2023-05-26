def solution(s):
    s = s.split(" ")
    l = len(s)
    answer = 0

    for i in range(l):
        if s[i] == 'Z':
            answer -= int(s[i - 1])
        else:
            answer += int(s[i])
    return answer