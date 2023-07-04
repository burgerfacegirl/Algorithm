def solution(strings, n):
    k = []
    for idx, word in enumerate(strings):
        k.append([word[n], idx])

    k.sort()
    temp = []
    for ss in k:
        temp.append([strings[ss[1]], ss[0]])

    temp.sort(key=lambda x: (x[1], x[0]))

    answer = []
    for word in temp:
        answer.append(word[0])
    return answer