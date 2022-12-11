#220913_boj_2178_미로탐색_실버1_BFS

# dfs로 푸니까 시간초과 뜸..
def dfs(i, j, s):
    global minV
    if i == N-1 and j == M-1:
        if minV > s + 1:                # 출발, 도착 포함이니까 s+1
            minV = s + 1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and miro[ni][nj] != 0 and visited[ni][nj] == 0:
                dfs(ni, nj, s+1)
        visited[i][j] = 0
        return


N,M = map(int,input().split())
miro = [list(map(int,input())) for _ in range(N)]

minV = N*M
visited = [[0] * M for _ in range(N)]
dfs(0, 0, 0)
print(minV)
print(visited)