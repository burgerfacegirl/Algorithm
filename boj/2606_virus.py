# 220913_boj_바이러스_실버3_DFS_BFS
# 다 못품 다시풀어라

# 1. dfs - 재귀로 풀기
def dfs(v):
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)

C = int(input())        # 컴퓨터 수  (정점 수)
E = int(input())        # 네트워크 수 (간선 수)
adjList = [[] for _ in range(C+1)]
visited = [0] * (C+1)
for _ in range(E):
    a, b = map(int,input().split())
    adjList[a].append(b)
    adjList[b].append(a)

dfs(1)                      # 1번 컴퓨터부터
print(visited.count(1)-1)   # 1번 컴퓨터 빼고 감염된(방문한) 노드 세줌