
# 자연수 N과 M
# 1부터 N까지 자연수 중 M개를 고른 수열
# 같은 수를 여러번 골라도 된다

N, M = map(int, input().split())
arr = [0 for _ in range(M)]

def recur(cur):
    if cur == M:
        print(*arr)
        return
    for i in range(1, N+1):
        arr[cur] = i
        recur(cur + 1)

recur(0)