# boj_15649_N과 M(1)

# N개 중 M개를 뽑는 중복 없는 순열 출력 (자연수 1부터)
# 4 2
# 1 2 ~ 4 2
N, M = map(int, input().split())
arr = [0 for _ in range(M)]
visited = [False for _ in range(N+1)]
def recur(cur):
    if cur == M:        # cur은 재귀 반복 횟수니까 몇개를 뽑을건지, start는 지금 뽑은 수
        print(*arr)
        return

    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        arr[cur] = i
        recur(cur + 1)
        visited[i] = False

recur(0)