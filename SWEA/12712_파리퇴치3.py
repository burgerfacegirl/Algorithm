# 추가문제 파리퇴치 3

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    maxV = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for k in range(4):
                for d in range(1, M):
                    ni = i + di[k] * d
                    nj = j + dj[k] * d
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if maxV < s:
                maxV = s

    maxV2 = 0
    for i in range(N):
        for j in range(N):
            s1 = arr[i][j]
            for di, dj in [[-1, 1], [1, -1], [-1,-1], [1,1]]:
                for d in range(1, M):
                    ni = i + di * d
                    nj = j + dj * d
                    if 0 <= ni < N and 0 <= nj < N:
                        s1 += arr[ni][nj]
            if maxV2 < s1:
                maxV2 = s1

    if maxV < maxV2:
        print(maxV2)
    else:
        print(maxV)