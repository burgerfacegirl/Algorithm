def solution(sizes):
    answer = 0
    for wh in sizes:
        wh.sort()

    maxH = -100
    maxW = -100
    for wh in sizes:
        if wh[0] > maxH:
            maxH = wh[0]
        if wh[1] > maxW:
            maxW = wh[1]

    answer = maxH * maxW

    return answer