# 추가문제 13837_각행의 구간합

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1):
        s = 0
        for j in range(M):
            s += arr[i][i+j]
            if maxV < s:
                maxV = s

    i = N-1
    J = N-1
    for i in range(N-1, N-M, -1):
        s = 0
        for j in range(i, N):
            s += arr[i][j]
        if maxV < s:
            maxV = s

    # while i >= N-M+1:
    #     s = 0
    #     for j in range(J, J-1, -1):
    #         s += arr[i][j]
    #     if maxV < s:
    #         maxV = s
    #     i -= 1
    #     j += 1


    print(f'#{tc} {maxV}')

