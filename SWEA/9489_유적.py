# IM 대비

T = int(int(input()))

for tc in range(1, T+1):
    N, M = map(int, input().split())
    land = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        cnt1 = 0
        for j in range(M):
            if land[i][j] == 1:
                cnt1 += 1
                if maxV < cnt1:
                    maxV = cnt1
            else:
                cnt1 = 0

    for j in range(M):
        cnt2 = 0
        for i in range(N):
            if land[i][j] == 1:
                cnt2 += 1
                if maxV < cnt2:
                    maxV = cnt2
            else:
                cnt2 = 0

    print(f'#{tc} {maxV}')