#220912_boj_16173_jumpking_실버4

def bfs(i, j, N):                           # i, j : 출발점 인덱스, N : 배열 크기
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i,j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if game[i][j] == -1:
            return "HaruHaru"
        move = game[i][j]
        for di, dj in [[1,0], [0,1]]:
            ni, nj = i + di * move, j + dj * move
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    # print(visited)
    # print(q)
    return "Hing"                       # 다 돌았는데 -1 못 만나면 도착지 못 가는거

import sys
N = int(sys.stdin.readline())
game = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]


print(bfs(0, 0, N))
