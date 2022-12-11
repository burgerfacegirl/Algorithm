#220917_boj_상근이의 여행_그래프이론,트리_실버4

# 구글링 한 dfs 재귀 코드
def travel(v, ans):
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            ans = travel(w, ans+1)
    return ans

T = int(input())

# 연결그래프라 ? input() 으로 하면 시간 초과 뜸 ㅡㅡ
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 국가의 수, M 비행기의 종류
    adjList = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)
    print(N-1)

# 최종 제출 코드
import sys

for tc in range(1, int(sys.stdin.readline())+1):
    N, M = map(int, sys.stdin.readline().split())    # N 국가의 수, M 비행기의 종류
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
    print(N-1)

# dfs 로 푼 첫 제출 코드 ( 시간 초과 )
def travel(N, v):
    global ans
    visited[v] = 1
    # stack.append(v)
    for w in adjList[v]:
        if visited[w] == 0:
            ans += 1
            travel(N, w)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 국가의 수, M 비행기의 종류
    adjList = [[] for _ in range(N+1)]
    # stack = []
    visited = [0] * (N+1)
    ans = 0
    for _ in range(M):
        a, b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)
    travel(N, 1)
    print(ans)