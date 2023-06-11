def solution(brown, yellow):
    area = brown + yellow
    answer = []

    for j in range(1, int(yellow ** 0.5) + 1):
        if yellow % j == 0:
            y_column = j
            y_row = yellow // j
        if (y_column + 2) * (y_row + 2) - yellow == brown:
            answer += [y_row + 2, y_column + 2]
            break
    return answer