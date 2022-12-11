# 221020_boj_17086_아기상어2_실버2

# def safe(i, j, dis):
#     global q, minD
#     q.append((i,j))
#     visited[i][j] = 1
#     while q:
#         i, j = q.pop(0)
#         for d_i, d_j in di,dj:
#             ni, nj = i+d_i, j+d_j
#             if 0<=ni<N and 0<=nj<M and visited[i][j] == 0:
#                 q.append((i,j))
#                 visited[i][j] = 1
#                 dis += 1

def dfs(i, j, cnt):
    global minD
    visited[i][j] = 1
    for d_i, d_j in dx:
        ni, nj = i+d_i, j+d_j
        if 0<=ni<N and 0<=nj<M and visited[i][j] == 0:
            # if minD > cnt:
            #     minD = cnt
            dfs(i, j, cnt+1)
            if sharks[ni][nj] == 1:
                return cnt

    # minD.append()



N, M = map(int,input().split())
sharks = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
minD = 1000000
dx = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]    # 위부터 시계방향
# dj = [0, 1, 1, 1, 0, -1, -1, -1]
q = []
distance = []

for i in range(N):
    for j in range(M):
        if sharks[i][j] == 1:
            print(dfs(i, j, 0))
            sharks[i][j] = 2

# print(dfs(0, 0, 3))