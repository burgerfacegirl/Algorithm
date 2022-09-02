# IM 추천문제(교수님) SWEA 13732.

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = 'yes'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                p = 0
                q = 0
                while arr[i][j+p] == '#':        # 행
                    p += 1
                    if j+p >= N:
                        break
                while arr[i+q][j] == '#':        # 열
                    q += 1
                    if i+q >= N:
                        break
                if p>0 and p == q:               # '#' 영역 가로칸수 세로칸수 같으면
                    # ans = 'yes'   /? fail 떴다가 이거 지우니까 됨
                    for k in range(p):
                        for h in range(q):
                            if arr[i+h][j+k] == '#':    # '#' 사각형 영역에 있는 '#' 다 0으로 지워주고
                                arr[i+h][j+k] = 0
                            elif arr[i+h][j+k] != '#':  # 정사각형 내부가 '#'이 아니면 ans = 'no'
                                ans = 'no'
                                break

                for i in range(N):                      # 정사각형 1개를 0으로 지웠는데 '#' 남아있으면 ans = 'no'
                    for j in range(N):
                        if arr[i][j] == '#':
                            ans = 'no'
                            break

        if ans == 'no':
            break


    print(f'#{tc} {ans}')



