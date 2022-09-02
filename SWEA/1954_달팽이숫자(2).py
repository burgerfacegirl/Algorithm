T = int(input())

for tc in range(1, T+1):
    N = int(input())

    snail = [[0] * 3 for _ in range(N)]

    di = [0, 1, 0, -1] # 우하좌상
    dj = [1, 0, -1, 0]

    i = j = ni = nj = 0
    k = 0
    m = 1

    while m < N*N:
        if snail[i][j] == 0:
            snail[i][j] = m

        else:
            ni = ni + di[k]
            nj = nj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0:
                m += 1
                snail[ni][nj] = m
            else:
                ni = ni - di[k]
                nj = nj - dj[k]
                k = (k+1)%4

    print(snail)

