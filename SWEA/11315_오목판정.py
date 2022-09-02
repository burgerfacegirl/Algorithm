# IM 대비 11315_오목판정

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 'NO'
    for i in range(N):                       # 가로세로
        check_r = 0
        check_c = 0
        for j in range(N):
            if arr[i][j] == 'o':
                check_r += 1
            if arr[i][j] == '.':
                check_r = 0
            if arr[j][i] == 'o':
                check_c += 1
            if arr[j][i] == '.':
                check_c = 0
            if check_r >= 5 or check_c >= 5:
                ans = 'YES'
                break
        if ans == 'YES':
            break

    for i in range(N):                      # 왼쪽 위 대각선
        for j in range(N):
            check_lx = 0
            if arr[i][j] == 'o':
                k = 0
                while 0 <= i + k < N and 0 <= j + k < N:
                    if arr[i + k][j + k] == 'o':
                        check_lx += 1
                    else:
                        check_lx = 0
                    k += 1
                    if check_lx >= 5:
                        ans = 'YES'
                        break
        if ans == 'YES':
            break

    for i in range(N):                      # 오른쪽 위 대각선
        for j in range(N-1, -1, -1):
            check_rx = 0
            if arr[i][j] == 'o':
                k = 0
                while 0 <= i + k < N and 0 <= j - k < N:
                    if arr[i + k][j - k] == 'o':
                        check_rx += 1
                    else:
                        check_rx = 0
                    k += 1
                    if check_rx >= 5:
                        ans = 'YES'
                        break
        if ans == 'YES':
            break
    #
    # for i in range(N):
    #     for j in range(N):
    #         cnt_rc: int = 0
    #         cnt_lc: int = 0
    #         for d in range(5):
    #             if 0 <= i + d < N and 0 <= j + d < N:
    #                 if arr[i + d][j + d] == 'o':
    #                     cnt_rc += 1
    #             if 0 <= i + d < N and 0 <= j - d < N:
    #                 if arr[i + d][j - d] == 'o':
    #                     cnt_lc += 1
    #
    #         if cnt_rc == 5 or cnt_lc == 5:
    #             ans = 'YES'

    print(f'#{tc} {ans}')