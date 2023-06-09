def solution(s):
    answer = 1
    stack = []
    s = list(s)
    while s:
        letter = s.pop()
        if len(stack) == 0 :
            stack.append(letter)
        else:
            if stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)

    if stack:
        answer = 0
    return answer

print(solution("cdcd"))