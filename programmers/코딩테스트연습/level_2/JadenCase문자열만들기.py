def solution(s):
    temp = s.split(" ")
    new = []
    for word in temp:
        tmp_s = ""
        if word and word[0].isalpha() and word[0].islower():
            tmp_s += word[0].upper()
            for m in word[1:]:
                if m.isupper():
                    tmp_s += m.lower()
                else:
                    tmp_s += m
            new.append(tmp_s)
        else:
            if word:
                tmp_s += word[0]
                for m in word[1:]:
                    if m.isupper():
                        tmp_s += m.lower()
                    else:
                        tmp_s += m
                new.append(tmp_s)
            else:
                new.append(word)

    answer = " ".join(new)
    return answer

