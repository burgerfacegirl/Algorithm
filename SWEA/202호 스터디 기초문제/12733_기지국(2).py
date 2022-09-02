# 202호 스터디 모의 12733_기지국

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = [0, 1, 0, -1]      # 우하좌상
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                R = 2
            elif arr[i][j] == 'B':  # B 기지국이면
                R = 3
            elif arr[i][j] == 'C':
                R = 4
            else:
                R = 1
            for p in range(1,R):
                for k in range(4):
                    if arr[i][j] == 'A':
                        ni, nj = i+di[k]*p, j+dj[k]*p
                        if 0<=ni<N and 0<=nj<N:
                            arr[ni][nj] = 0
                    elif arr[i][j] == 'B':                      # B 기지국이면
                        ni, nj = i+di[k]*p, j+dj[k]*p
                        if 0 <= ni < N and 0 <= nj <N:
                            arr[ni][nj] = 0
                    elif arr[i][j] == 'C':
                        ni, nj = i+di[k]*p, j+dj[k]*p
                        if 0 <= ni < N and 0 <= nj < N:
                            arr[ni][nj] = 0

    ucHouse = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':                                # 0으로 안 바뀌고(커버 안 되고) 남아있는 H 숫자 세줌
                ucHouse += 1
    print(f'#{tc} {ucHouse}')


