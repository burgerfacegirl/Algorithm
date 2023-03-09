# boj_15652_N과M(4)

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

N, M = map(int, input().split())
arr = [0 for i in range(M)]

def recur(cur, start):
    if cur == M:
        print(*arr)
        return

    for i in range(start, N+1):
        arr[cur] = i
        recur(cur + 1, i)

recur(0, 1)

