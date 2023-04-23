# boj_2644_촌수계산

N = int(input())
a, b = map(int, input().split())
M = int(input())
nvx = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())

    nvx[x].append(y)
    nvx[y].append(x)
ans = -1
def dfs(cur, cnt):
    global ans
    visited[cur] = 1
    if cur == a:
        ans = cnt
        return
    for node in nvx[cur]:
        if not visited[node]:
            dfs(node, cnt+1)
dfs(b, 0)
print(ans)

