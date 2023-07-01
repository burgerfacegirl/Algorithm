def solution(s, n):
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = "abcdefghijklmnopqrstuvwxyz"
    answer = ''
    m = len(big)

    for spell in s:
        if spell.isupper():
            idx = big.index(spell)
            if idx + n > m - 1:
                i = idx + n - m
                answer += big[i]
            else:
                answer += big[idx + n]
        elif spell.islower():
            idx = small.index(spell)
            if idx + n > m - 1:
                i = idx + n - m
                answer += small[i]
            else:
                answer += small[idx + n]
        else:
            answer += " "

    return answer

print(solution("z", 1))