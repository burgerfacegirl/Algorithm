N, M = map(int, input().split())
arr = [0 for _ in range(M)]

def recur(cur):
    if cur == M:
        print(*arr)
        return

    for i in range(N):
        arr[cur] = i
        recur(cur+1)

recur(0)