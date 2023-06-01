from collections import deque

# 가중치가 없는 그래프에서 최단 거리 구할때 => bfs
# 다익스트라는 음이 아닌 가중치가 있는 그래프에서 최단거리 구할때

# boj_바이러스

n = int(input())
m = int(input())
v = [[] for i in range(n+1)]
# 간선은 dfs랑 똑같이 함
visited = [False for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

que = deque()

que.append(1)
while len(que) > 0:
    cur = que[0]
    que.popleft()

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        que.append(nxt)
        visited[nxt] = True

# 중요한 건 방문 처리 시점 다시 넣지 않도록 (visited[cur] = True 해주는 시점)
# que.append 랑 visited를 무조건 같이해준다고 생각하면 됨
# 출발점에서 특정 지점으로 가는 최소 간선의 개수(최단거리) 같은걸 구할때는 bfs 만 가능
# dfs는 최단거리 보장 못함



















