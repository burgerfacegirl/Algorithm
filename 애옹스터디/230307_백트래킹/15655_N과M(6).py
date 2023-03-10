# boj_15655_N과M(6)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
arr = [0 for i in range(M)]
nums.sort()

def recur(cur, start):
    if cur == M:
        print(*arr)
        return

    for i in range(start, N):
        arr[cur] = nums[i]
        recur(cur + 1, i + 1)

recur(0, 0)