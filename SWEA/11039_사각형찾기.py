# 추가문제 11039_사각형찾기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]        # 2차원 배열

    max_s = 0                               # 답 / 직사각형 가로 세로 칸수 곱한 값 중 최댓값
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:              # 1이면
                p = 0                       # 가로 칸수
                while arr[i][j+p] == 1:     # 열 index+1 하면서 그 행에서 값이 1인동안 가로 칸수 +1 (가로 칸수 세줌)
                    p += 1

                q = 0                       # 세로 칸수
                while arr[i+q][j] == 1:     # 행 index+1 하면서 그 열에서 값이 1인동안 세로 칸수 +1 (세로 칸수 세줌)
                    q += 1

                square = p*q                # 직사각형 넓이

                if max_s < square:          # 최댓값 갱신
                    max_s = square

                for k in range(p):          # 넓이 구한 직사각형 영역은 값 0으로 바꿈(지워줌)
                    for o in range(q):
                        arr[i+o][j+k] = 0

    print(f'#{tc} {max_s}')




