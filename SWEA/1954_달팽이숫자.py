# 220810_List2. 1954. 달팽이 숫자

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail = list([0]*N for _ in range(N))
    k = 0                # 방향 전환
    p = 1
    i = j = ni = nj = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while p < N*N:
        if snail[i][j] == 0:
            snail[i][j] = p

        else:
            ni = ni + di[k]
            nj = nj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0:
                p += 1
                snail[ni][nj] = p
            else:
                ni -= di[k]
                nj -= dj[k]
                k = (k+1) % 4

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()