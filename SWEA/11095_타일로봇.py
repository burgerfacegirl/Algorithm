# 추가문제 11095_타일로봇

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    wall = list([0] * 10 for _ in range(10))                    # 벽 / 10*10 2차원 배열
    arr = [list(map(int,input().split())) for _ in range(N)]    # 왼쪽 위 모서리 인덱스, 오른쪽 아래 모서리 인덱스 묶어서 2차원 배열로

    s = 0
    for i in range(N):
        box1 = arr[i]                                           # 각 영역 별로
        r1, c1, r2, c2 = box1                                   # 시작점 행,열 인덱스(r1, c1)/ 끝점 행,열 인덱스(r2, c2)
        for j in range(r1, r2+1):                               # wall 의 해당 영역 값 1로 바꿔줌
            for k in range(c1, c2+1):
                wall[j][k] = 1

    cnt = 0
    for i in range(10):                                         # wall 에서 1 개수 카운트
        for j in range(10):
            if wall[i][j] == 1:
                cnt += 1

    print(f'#{tc} {cnt}')