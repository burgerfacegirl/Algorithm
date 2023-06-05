def solution(s):
    answer = True

    s = list(s)
    close = 0
    open = 0
    cnt = 0
    before = False

    if s[-1] == "(" or s[0] == ")":
        answer = False
    else:
        while s:
            #             다른 괄호가 2번 나오면 그때까지 쌓인 close/open 개수 비교
            letter = s.pop()
            if before:
                if before != letter:
                    cnt += 1
            elif before == False and s[-1] != s[-2]:
                cnt += 1

            if letter == ")":
                close += 1
            elif letter == "(":
                open += 1
            before = letter
            if cnt == 2:
                if close != open:
                    answer = False
                    break
                else:
                    cnt = 0
                    close = 0
                    open = 0

    return answer