def solution(s):
    answer = True

    closed = []

    if s[0] == ")" or s[-1] == "(":
        answer = False
    else:
        while s:
            letter = s.pop()

            if letter == ")":
                closed.append(letter)
            else:
                if closed:
                    closed.pop()
                    s.pop()
                else:
                    answer = False
                    break

            if answer == False:
                break

        if closed:
            answer = False

    return answer


