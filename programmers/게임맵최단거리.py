# dfs,bfs level2


def solution(maps):
    cnt = 1
    stack = []
    stack.append([0, 0, 1])
    answer = 1000000
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    i = j = 0
    p = N-1     # 상대편 위치 행
    q = M-1     # 상대편 위치 열
    while stack:
        i, j, cnt = stack.pop()
        for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                stack.append([ni, nj, cnt+1])
                visited[ni][nj] = 1
                i, j, cnt = ni, nj, cnt+1
                if i == p and j == q :
                    if answer > cnt:
                        answer = cnt

    if answer == 1000000:
        answer = -1
    return answer

maps = [[1, 1, 1], [1, 0, 0], [1, 1, 1]]
print(solution(maps))