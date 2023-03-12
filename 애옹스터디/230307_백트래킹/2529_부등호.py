# boj_2529_부등호

k = int(input())
signs = list(input().split())
N = 10
M = k+1
arr = [0 for i in range(M)]
visited = [False for i in range(N)]
ans = []
def recur(cur):
    if cur == M:
        for j in range(k):
            if (signs[j] == '<' and arr[j] >= arr[j+1]) or (signs[j] == '>' and arr[j] <= arr[j+1]):
                return
        ans.append("".join(map(str, arr)))
        return

    for i in range(N):
        if visited[i] == True:
            continue
        arr[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0)
print(ans[-1])
print(ans[0])
