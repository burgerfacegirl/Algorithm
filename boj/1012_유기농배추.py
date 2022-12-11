# 220929_boj_1012_유기농배추_실버2
def bfs(i,j):
    q = []
    q.append((i,j))
    while q:
        i, j = q.pop(0)
        for di,dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and field[ni][nj] == 1:
                field[ni][nj] = 0
                q.append((ni, nj))

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int,input().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        j, i = map(int,input().split())
        field[i][j] = 1

    worm = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                bfs(i,j)
                worm += 1

    print(worm)
