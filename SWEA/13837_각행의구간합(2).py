# 각행의 구간합 방법2

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        s = 0
        for j in range(i, i+K):
            if j < N:
                s += arr[i][j]
        if maxV < s:
            maxV = s


    print(f'#{tc} {maxV}')
