# 202호 스터디 모의 problem 12733_기지국

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = [0, 1, 0, -1]  # 우하좌상
    dj = [1, 0, -1, 0]

    for i in range(N):
        p = 1  # B 기지국 커버 범위
        q = 1  # C 기지국 커버 범위
        for j in range(N):
            if arr[i][j] == 'A':  # A 기지국이면
                for k in range(4):  # 상하좌우 한칸씩 0으로 바꿔줌(커버된 집 표시)
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        arr[ni][nj] = 0
            elif arr[i][j] == 'B':  # B 기지국이면
                while p < 3:  # 상하좌우 +2칸까지 0으로 바꿔줌(커버된 집 표시)
                    for k in range(4):
                        ni, nj = i + di[k] * p, j + dj[k] * p
                        if 0 <= ni < N and 0 <= nj < N:
                            arr[ni][nj] = 0
                    p += 1
            elif arr[i][j] == 'C':
                while q < 4:  # C 기지국이면
                    for k in range(4):  # 상하좌우 +3칸까지 0으로 바꿔줌(커버된 집 표시)
                        ni, nj = i + di[k] * q, j + dj[k] * q
                        if 0 <= ni < N and 0 <= nj < N:
                            arr[ni][nj] = 0
                    q += 1

    ucHouse = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':  # 0으로 안 바뀌고(커버 안 되고) 남아있는 H 숫자 세줌
                ucHouse += 1
    print(f'#{tc} {ucHouse}')