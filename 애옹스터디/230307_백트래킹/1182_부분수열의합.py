# boj_1182_부분수열의합

N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
visited = [False for i in range(N)]
def recur(cur, start):
    global cnt
    if cur == M:
        total = sum(arr)
        if total == S:
            cnt += 1
        return
    for i in range(start, N):
        arr[cur] = nums[i]
        recur(cur + 1, i + 1)

for j in range(1, N+1):
    M = j
    arr = [0 for i in range(j)]
    recur(0, 0)

print(cnt)
