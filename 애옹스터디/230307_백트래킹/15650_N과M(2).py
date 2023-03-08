# boj_15650_N과M(2)

# 자연수 N, M 중 중복 없이 M개를 고른 오름차순 수열

N, M = map(int, input().split())
arr = [0 for _ in range(M)]

def recur(cur, start):
    if cur == M:
        print(*arr)
        return

    for i in range(start, N+1):
        arr[cur] = i
        recur(cur+1, i+1)

recur(0, 1)