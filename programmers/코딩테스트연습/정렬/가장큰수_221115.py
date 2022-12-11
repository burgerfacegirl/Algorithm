# 221115 가장 큰 수 https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    N = len(numbers)
    for i in range(N):
        numbers[i] = str(numbers[i])

    numbers = sorted(numbers, key = lambda x : int(x[0]), reverse=True)

    for i in range(N):
        if numbers[i] == numbers[i+1]:
            pass

    return numbers


# print(solution([3, 30, 34, 5, 9]))
# print(solution([6, 10, 2]))