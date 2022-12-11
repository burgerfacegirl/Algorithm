# 220913_boj_14248_점프 점프_silver2
def dfs(s):
    global ans
    visited[s] = 1                  # 방문 표시
    ans += 1                        # 방문 가능한 돌 개수
    for w in adjList[s]:
        if visited[w] == 0:         # 방문 안 했으면
            # visited[w] = 1          # 방문
            dfs(w)                  # w 방문하고, w와 인접한 곳 방문하기 위해 다시 호출


N = int(input())
rocks = [0] + list(map(int,input().split()))
s = int(input())
adjList = [[] for _ in range(N+1)]
# print(rocks)
visited = [0] * (N+1)
ans = 0
for i in range(1, N+1):                 # 인접리스트 만들기
    # a, b = i-rocks[i], i+rocks[i]
    if 0 < i-rocks[i] <= N:
        adjList[i].append(i-rocks[i])
    if 0 < i+rocks[i] <= N:
        adjList[i].append(i+rocks[i])

dfs(s)
print(ans)
