def canigo(i, j):
    global ans
    if miro[i][j] == 3:
        ans = 1
    else:
        visited[i][j] = 1
        for di, dj in [[1,0], [0,1], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and miro[ni][nj] != 1:
                visited[ni][nj] = 1
                canigo(ni, nj)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]
    stack = []
    visited = [[0] * (N+1) for _ in range(N)]
    si = sj = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                si = i
                sj = j
                break
        if si:
            break
    ans = 0
    canigo(si, sj)
    print(f'#{tc} {ans}')