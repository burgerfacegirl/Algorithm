# 추가문제

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pang = [list(map(int,input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    maxV = 0                                         # 날리는 꽃가루 합 중 최댓값
    for i in range(N):
        for j in range(M):
            s = pang[i][j]                           # 기준 풍선 꽃가루로 시작
            for p in range(1, pang[i][j]+1):         # 기준 풍선에 든 꽃가루만큼
                for k in range(4):                   # 상하좌우로 더해줌
                    ni = i + di[k]*p
                    nj = j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < M:  # 행열 index가 pang 범위 벗어나지 않을 때
                        s += pang[ni][nj]
            if maxV < s:                             # 최댓값 갱신
                maxV = s

    print(f'#{tc} {maxV}')