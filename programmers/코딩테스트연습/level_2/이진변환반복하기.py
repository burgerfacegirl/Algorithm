def solution(s):
    cnt_zero = 0
    cnt_bt = 0

    while int(s) != 1:
        tmp = ""
        for letter in s:
            if letter == "0":
                cnt_zero += 1
            else:
                tmp += letter

        num = len(tmp)

        after_bt = ""

        while num:
            after_bt += str(num % 2)
            num //= 2

        cnt_bt += 1
        s = after_bt[::-1]

    answer = [cnt_bt, cnt_zero]
    return answer

print(solution("110010101001"))