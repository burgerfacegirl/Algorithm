# 추가문제 11042. 부분 배열의 합

T = int(input())

for tc in range(1, T+1):
    N, n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-n+1):              # n*m이 돌아다닐 행 범위
        for j in range(N-m+1):          # n*m이 돌아다닐 열 범위
            s = 0                       # 영역합 / 시작점 바뀔때마다 영역 합 초기화
            for p in range(n):
                for q in range(m):
                    s += arr[i+p][j+q]  # n*m 영역합 더해줌
            if maxV < s:                # 다른 열로 넘어갈때마다 최댓값 갱신           maxV = s

    print(f'#{tc} {maxV}')