# 추가문제 12726.토글

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    k = 1
    while k <= M:                                   # 1초부터 M초까지
        for i in range(N):
            for j in range(N):
                if M%k == 0 or k == M:              # M이 k의 배수 or k == M초인지 먼저 검사
                    if arr[i][j] == 0:              # 전체 토글
                        arr[i][j] = 1
                    else:
                        arr[i][j] = 0
                elif (i+j+2)%k == 0 or i+j+2 == k:  # 위 조건에 해당하지 않는 경우 중 i+j == k 이거나 k의 배수인 경우 / 문제에서 인덱스 1부터 시작하니까 조건에 2 더해줌
                    if arr[i][j] == 0:              # 해당 영역 토글
                        arr[i][j] = 1
                    else:
                        arr[i][j] = 0
        k += 1                                      # 2차원 배열 전체 돌고 +1초

    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                ans += 1

    print(f'#{tc} {ans}')