# LEVEL 1 실패율_정렬

def solution(N, stages):
    challengers = len(stages)
    cnt = [[0, 0] for _ in range(N+1)]

    for i in range(1, N+1):
        cnt[i][1] = i
        noclear = 0                     # 스테이지에 도달 했으나 아직 클리어X 플레이어 수
        onstage = 0                     # 스테이지에 도달한 플레이어 수
        for j in range(challengers):
            if stages[j] == i:
                noclear += 1
            if stages[j] >= i:          # 해당 스테이지에 도전 중인 사람도 스테이지에 도달한 플레이어 수에 세줘야함 (elifX)
                onstage += 1
        if onstage != 0:
            cnt[i][0] = noclear/onstage
        else:
            cnt[i][0] = 0

    cnt = cnt[1:]
    answer = []
    # sorted_cnt = sorted(cnt, key = lambda x: (-x[0], cnt.index(x[0])))
    sorted_cnt = sorted(cnt, key = lambda x: [-x[0], x[1]])
    for i in range(N):
        answer.append(sorted_cnt[i][1])

    # while True:
    #     for i in range(1, N+1):
    #         maxF = max(cnt)
    #         if cnt[i] == maxF:
    #             answer.append(i)
    #             cnt[i] = -1
    #     if len(answer) == N:
    #         break
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))


# 패스코드
def solution(N, stages):
    challengers = len(stages)
    cnt = [[0, 0] for _ in range(N + 1)]
    onstage = challengers   # 스테이지에 도달한 플레이어 수
    for i in range(1, N + 1):
        cnt[i][1] = i
        noclear = 0  # 스테이지에 도달 했으나 아직 클리어X 플레이어 수
        for j in range(challengers):
            if stages[j] == i:
                noclear += 1
        if onstage == 0:
            cnt[i][0] = 0
        else:
            cnt[i][0] = noclear / onstage
        onstage = onstage - noclear

    cnt = cnt[1:]
    answer = [0] * N
    sorted_cnt = sorted(cnt, key=lambda x: [-x[0], x[1]])

    for i in range(N):
        answer[i] = sorted_cnt[i][1]

    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))