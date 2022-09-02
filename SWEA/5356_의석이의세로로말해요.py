# 추가문제 5356. 의석이의 세로로 말해요

T = int(input())
N = 5

for tc in range(1, T+1):
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        if len(arr[i]) < 15:                # 모든 단어에 대해 최장 문자열 길이 15까지 빈칸 0으로 채워줌
            while len(arr[i]) < 15:
                arr[i].append(0)

    print(f'#{tc}', end = ' ')
    for j in range(15):
        for i in range(N):                  # 0이 아닌 글자 세로로 출력
            if arr[i][j] != 0:
                print(arr[i][j], end = '')
    print()
