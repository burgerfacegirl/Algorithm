def solution(n):
    answer = 0

    for i in range(1, n + 1):
        cnt = i
        for j in range(i + 1, n + 1):
            cnt += j
            if cnt == n:
                answer += 1
            if cnt > n:
                break
    #   자기자신 하나 더해줌
    return answer + 1