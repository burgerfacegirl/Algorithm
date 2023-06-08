def solution(x):
    answer = True
    n = str(x)
    tonum = 0
    for s in n:
        tonum += int(s)

    if x % tonum:
        answer = False

    return answer