# 추가문제 11045. 이웃 원소의 합

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]    # N*N 2차원 배열

    di = [0, 1, 0, -1]              # 우하좌상
    dj = [1, 0, -1, 0]

    maxV = 0
    for i in range(N):
        for j in range(N):          # 2차원 배열 모든 원소에 접근
            s = 0                   # arr의 다른 원소로 넘어올때마다 이웃 원소의 합 초기화
            for k in range(4):      # 우, 하, 좌, 상
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N :      # 유효한 인덱스면
                    s += arr[ni][nj]
            if maxV < s:            # 이웃한 네 방향 원소 모두 돌고 maxV 값 갱신
                maxV = s

    print(f'#{tc} {maxV}')