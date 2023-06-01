def solution(array, n):
    answer = 0
    array.sort()

    min_d = 1000

    for num in array:
        if abs(n-num) < min_d:
            min_d = abs(n-num)
            answer = num

    return answer

print(solution([10, 11, 12], 12))