# 추가문제 9490. 풍선팡

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    di = [0, 1, 0, -1] # 우 하 좌 상
    dj = [1, 0, -1, 0]
    maxV = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for p in range(1,arr[i][j]+1):
                k = 0
                while k < 4:
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if 0 <= ni < N and 0 <= nj < M:
                        s += arr[ni][nj]
                    k += 1
            if maxV < s:
                maxV = s
    print(maxV)


