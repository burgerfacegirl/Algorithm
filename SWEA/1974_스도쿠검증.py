# 추가문제1. 1974. 스도쿠 검증

T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]  # 2차원 배열로 받아줌

    ans = 1
    for i in range(9):                  # 행 검사
        count = [0] * 10                # 행마다 count 배열 초기화
        for j in range(9):
            count[sudoku[i][j]] += 1
        for number in count:            # 겹치는 숫자가 있으면 count[숫자]가 1보다 크니까 그때 ans=0
            if number > 1:
                ans = 0

    for i in range(9):                  # 열 검사
        count = [0] * 10                # 열마다 count 배열 초기화
        for j in range(9):
            count[sudoku[j][i]] += 1
        for number in count:
            if number > 1:
                ans = 0

    for i in range(0, 7, 3):            # 3*3 격자가 돌아다닐 범위(index 6까지, i = 0,3,6)
        for j in range(0, 7, 3):
            count = [0] * 10
            for p in range(3):
                for q in range(3):
                    count[sudoku[i+p][j+q]] += 1
            for number in count:
                if number > 1:
                    ans = 0

    print(f'#{tc} {ans}')