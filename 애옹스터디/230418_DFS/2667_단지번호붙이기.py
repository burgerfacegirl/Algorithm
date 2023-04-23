# boj_2667_단지번호붙이기

N = int(input())
danji = []
visited = [[0] * N for _ in range(N)]

for _ in range(N):
    danji.append(list(map(int, input())))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

houses = []
cnt = 0
def dfs(cur_i, cur_j):
    global cnt
    visited[cur_i][cur_j] = 1
    cnt += 1

    for i in range(4):
        ni = cur_i + di[i]
        nj = cur_j + dj[i]
        if 0 <= ni < N and 0 <= nj < N and danji[ni][nj] and visited[ni][nj] == 0:
            dfs(ni, nj)

for i in range(N):
    for j in range(N):
        if danji[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            houses.append(cnt)
            cnt = 0

houses.sort()
print(len(houses))
for house in houses:
    print(house)