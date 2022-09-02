# 추가문제 10759. 색칠하기2

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    paper = [[0]*10 for _ in range(10)]
    colors = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        r1, c1, r2, c2, color = colors[i]
        for p in range(r1, r2+1):
            for q in range(c1, c2+1):
                if paper[p][q] == 0 or paper[p][q] == color:
                    paper[p][q] = color
                else:
                    paper[p][q] = 3

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 0
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1 or paper[i][j] == 2:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<=ni<10 and 0<=nj<10:
                        if paper[ni][nj] != 3 and paper[ni][nj] != paper[i][j]:
                            cnt += 1
                    else:
                        cnt += 1

            elif paper[i][j] == 3:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<=ni<10 and 0<=nj<10:
                        if paper[ni][nj] == 1 or paper[ni][nj] == 2:
                            cnt += 1

    print(f'#{tc} {cnt}')