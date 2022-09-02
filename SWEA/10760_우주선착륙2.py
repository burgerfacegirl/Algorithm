# 추가문제 10760_우주선착륙2

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    mars = [list(map(int,input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]      # 우하좌상
    dj = [1, 0, -1, 0]
    di_2 = [-1, -1, 1, 1]   # 대각선 행
    dj_2 = [1, -1, -1, 1]   # 대각선 열

    ans = 0                                             # 예비 후보지의 개수
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if mars[ni][nj] < mars[i][j]:       # 상하좌우 중 값이 더 작은 지역이 있으면 cnt +1
                        cnt += 1
            for q in range(4):
                ni = i + di_2[q]
                nj = j + dj_2[q]
                if 0 <= ni < N and 0 <= nj < M:
                    if mars[ni][nj] < mars[i][j]:
                        cnt += 1                        # 인접한 대각선 영역 중 값이 더 작은 지역이 있으면 cnt +1
            if cnt >= 4:                                # 값이 더 작은 지역이 4개 이상이면
                ans += 1                                # 후보지 개수 +1

    print(f'#{tc} {ans}')