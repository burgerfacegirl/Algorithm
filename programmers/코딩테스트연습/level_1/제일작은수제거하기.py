def solution(arr):
    answer = []
    n = min(arr)
    for num in arr:
        if num != n:
            answer.append(num)

    if len(answer) == 0:
        answer = [-1]

    return answer