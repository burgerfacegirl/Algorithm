# boj_2606_바이러스

n = int(input())
m = int(input())
vx = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = -1

for i in range(m):
    a, b = map(int, input().split())

    vx[a].append(b)
    vx[b].append(a)

def dfs(cur):
    global cnt
    visited[cur] = True

    cnt += 1
    for node in vx[cur]:
        if visited[node]:
            continue
        dfs(node)

dfs(1)
print(cnt)