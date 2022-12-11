#220918_boj_11724_연결요소의개수_DFS BFS 등등_실버2

import sys
sys.setrecursionlimit(5000)

def dfs(v):
    visited[v] = 1                  # 방문표시

    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)


N, M = map(int, input().split())    # 정점의 개수 N, 간선의 개수 M
adjList = [[] for _ in range(N+1)]  # 정점의 개수+1만큼 (인덱스 그대로 쓰기 위해서)
visited = [0] * (N+1)
cnt = 0                             # 연결 요소 개수

for i in range(M):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

for i in range(1, N+1):
    if visited[i] == 0:         # 방문 안했는데
        # 아래 if 부분 써서 냈는데 없어도 됨 어차피 방문 안했으면 호출해서 +1 되니까 (시간 줄이려고 쓴건가?)
        if adjList[i] == []:
            cnt += 1            # 연결된 정점 없으면(혼자 있는거) cnt += 1
            visited[i] = 1      # 방문 표시
        else:                   # 연결된 정점 있으면
            dfs(i)              # 함수 호출, 호출 됐을 때 i와 연결된 정점들은 다 방문 처리 되니까 다시 호출 안됨
            cnt += 1            # 연결 요소 개수 +1

print(cnt)