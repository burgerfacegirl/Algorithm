# IM대비 문제 5431.민석이의 과제 체크하기

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    students = [_ for _ in range(1, N+1)]
    done = list(map(int,input().split()))


    # for i in range(M-1, -1, -1):                          # 버블정렬
    #     for j in range(M-1):
    #         if done[j] > done[j+1]:
    #             done[j], done[j+1] = done[j+1], done[j]

    no = []
    # i = 0
    #
    # for j in range(M):
    #     for i in range(N):
    #         if done[j] == students[i]:
    #             students.pop(i)
    #
    for i in students:
        if i not in done:
            no.append(i)
    print(f'#{tc}', end = ' ')
    print(*no)


