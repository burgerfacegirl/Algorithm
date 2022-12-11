#220919_1388_바닥장식_실버3

N, M = map(int, input().split()) # 방 바닥 세로 크기 N, 가로 크기 M

floor = [list(input()) for _ in range(N)]

cnt_r = 0                                   # 행 판자 개수 (-)

for i in range(N):
    r = 0                                   # 전에 '-'가 있었는지 표시 / 행 바뀌면 초기화
    for j in range(M):
        if floor[i][j] == '-':              # '-'이면 r = 1
            r = 1
        if r == 1 and floor[i][j] == '|':   # 이전에 '-'가 있는 상태로 '|'를 만나면 판자 개수 1 더해주고
            cnt_r += 1
            r = 0                           # r 초기화
        elif r == 1 and j == M-1:           # 이전에 '-'가 있는 상태로 행 끝나면 판자 개수 1 더해줌
            cnt_r += 1

cnt_c = 0                                   # 열 판자 개수 (|)

for i in range(M):                          # 행이랑 같은 방식으로 열도 세줌
    c = 0
    for j in range(N):
        if floor[j][i] == '|':
            c = 1
        if c == 1 and floor[j][i] == '-':
            cnt_c += 1
            c = 0
        elif c == 1 and j == N-1:
            cnt_c += 1

print(cnt_r+cnt_c)