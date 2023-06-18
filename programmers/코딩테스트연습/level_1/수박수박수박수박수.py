def solution(n):
    watermelon = "수박"
    answer = ''
    for i in range(n):
        answer += watermelon[i%2]
    return answer