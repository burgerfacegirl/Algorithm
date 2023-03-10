# boj_15656_N과M(7)

N,M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = [0 for i in range(M)]

def recur(cur):
    if cur == M:
        print(*arr)
        return

    for i in range(N):
        arr[cur] = nums[i]
        recur(cur + 1)

recur(0)
