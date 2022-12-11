#220919_나이트의이동_실버1
from collections import deque
def bfs(si, sj, ei, ej):
    q = []
    q.append((si, sj))
    chess[si][sj] = 1

    while q:
        si, sj = q.pop(0)
        # print(i, j)
        if si == ei and sj == ej:       # 이동하려는 칸에 도달하면
            print(chess[si][sj]-1)
        for di, dj in d:
            ni, nj = si + di, sj + dj
            if 0<=ni<I and 0<=nj<I and chess[ni][nj] == 0:
                chess[ni][nj] = chess[si][sj] + 1
                q.append((ni, nj))


# 시계방향
d = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1]]

T = int(input())
for tc in range(1, T+1):
    I = int(input())                        # 체스 판 변의 길이
    chess = [[0] * I for _ in range(I)]
    # visited = [[0] * I for _ in range(I)]
    si, sj = map(int,input().split())   # 시작점 인덱스
    ei, ej = map(int,input().split())   # 도착점 인덱스

    bfs(si, sj, ei, ej)

