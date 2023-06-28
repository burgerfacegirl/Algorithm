def solution(s):
    s_list = s.split(" ")
    answer_list = []
    for str in s_list:
        s = ''
        for i in range(len(str)):
            if i % 2:
                s += str[i].lower()
            else:
                s += str[i].upper()
        answer_list.append(s)

    return " ".join(answer_list)