# boj_15657_N과M(8)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = [0 for i in range(M)]

def recur(cur, start):
    if cur == M:
        print(*arr)
        return
    for i in range(start, N):
        arr[cur] = nums[i]
        recur(cur+1, i)

recur(0, 0)