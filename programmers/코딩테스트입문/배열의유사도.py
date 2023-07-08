def solution(s1, s2):
    answer = 0
    n = len(s1)
    m = len(s2)
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                answer += 1
    return answer