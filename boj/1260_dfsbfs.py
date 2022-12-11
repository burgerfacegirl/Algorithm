# 220912_boj_1260_DFS와 BFS_실버2

def dfs(V):
    print(V, end=' ')
    visited[V] = 1
    for w in adjList[V]:
        if visited[w] == 0 :
            dfs(w)

def bfs(V):
    visited_b = [0] * (N+1)
    q = []
    q.append(V)
    while q:
        t = q.pop(0)
        if visited_b[t] == 0:
            visited_b[t] = 1
            print(t, end=' ')
            for i in adjList[t]:
                if visited_b[i] == 0:
                    # print(w, end=' ')
                    q.append(i)
    #             visited_b[w] = 1
    #     for p in adjList[V]:
    #         for k in adjList[p]:
    #             if visited_b[k] == 0 and k not in q:
    #                 q.append(k)
    #             # bfs(w)
    # print(q)

N, M, V = map(int,input().split())
visited = [0] * (N+1)
# visited_b = [0] * (N+1)
q = []
adjList = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    adjList[a].append(b)
    adjList[b].append(a)

for k in adjList:
    k.sort()

# adjList = sorted(adjList)
dfs(V)
print()
# print(adjList)
bfs(V)