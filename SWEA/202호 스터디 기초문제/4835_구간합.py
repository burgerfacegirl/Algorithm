# 구간합

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    maxV = 0
    minV = 1000000

    for i in range(N-M+1):          # i 값 시작 구간
        s = 0                       # 새로운 구간합 구할때마다 구간합 초기화 (012->123으로 갈때)
        for j in range(i, i+M):     # i~i+M 까지를 N-M+1 범위 안에서 더해줌(012,123,234...)
            s += arr[j]
        if maxV < s:                # 비교해서 구간합이 더 크면 maxV 갱신
            maxV = s
        if minV >= s:               # 비교해서 구간합이 더 작으면 minV 갱신
            minV = s

    print(f'#{tc} {maxV-minV}')

