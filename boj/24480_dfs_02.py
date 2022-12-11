import sys
sys.setrecursionlimit(10000000)

def dfs(R):
    global v
    visited[R] = v
    v += 1                          # 방문 순서 기록
    for i in adjList[R]:
        if visited[i] == 0:
            dfs(i)

N, M, R = map(int,sys.stdin.readline().split())
visited = [0] * (N+1)
v = 1

adjList = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    adjList[a].append(b)
    adjList[b].append(a)

for k in adjList:
    k.sort(reverse=True)

dfs(R)

for i in range(1,N+1):
    print(visited[i])