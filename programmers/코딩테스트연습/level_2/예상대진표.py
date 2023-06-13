def solution(n, a, b):
    N = [i for i in range(1, n + 1)]
    winners = []
    answer = 0
    flag = True
    cnt = 0

    while flag:
        idx_a, idx_b = N.index(a), N.index(b)
        if idx_a // 2 == idx_b // 2:
            cnt += 1
            answer = cnt
            flag = False
            break
        for i in range(0, len(N), 2):
            if i == idx_a or i + 1 == idx_a:
                winners.append(a)
            elif i == idx_b or i + 1 == idx_b:
                winners.append(b)
            else:
                winners.append(N[i])
        cnt += 1
        N = winners
        winners = []


    return answer

print(solution(8, 4, 7))