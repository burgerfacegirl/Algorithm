# 220819_문제풀이1 1979.어디에 단어가 들어갈 수 있을까

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        cnt_row = 0
        cnt_column = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt_row += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt_row == M:
                    ans += 1
                cnt_row = 0

            if puzzle[j][i] == 1:
                cnt_column += 1
            if puzzle[j][i] == 0 or j == N - 1:
                if cnt_column == M:
                    ans += 1
                cnt_column = 0
    print(f'#{tc} {ans}')