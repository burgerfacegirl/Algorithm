# boj_11724_연결 요소의 개수

N, M = map(int,input().split())
nvx = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())

    nvx[a].append(b)
    nvx[b].append(a)


def dfs(cur):
    visited[cur] = True

    for node in nvx[cur]:
        if visited[node] == False:
            dfs(node)

cnt = 0
for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)