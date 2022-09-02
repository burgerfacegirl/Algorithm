# 추가문제. 11094_가로세로의 최대합

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0                        # 칸을 포함하는 가로 행과 세로 열 값 총합의 최댓값
    for i in range(N):
        for j in range(N):
            s = 0                   # 각 칸을 포함하는 행 + 열 합
            for k in range(N):
                s += arr[i][k]      # 해당 칸을 포함하는 행 합 (행 index는 그대로 두고 열 index만 0 -> N-1)
                s += arr[k][j]      # 해당 칸을 포함하는 열 합 (열 index는 그대로 두고 행 index만 0 -> N-1)
            s -= arr[i][j]          # 기준 칸은 2번 더해지니까 한번 빼줌
            if maxV < s:            # 최댓값 갱신
                maxV = s

    print(f'#{tc} {maxV}')
