# boj_15654_N과 M(5)

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열
# 중복 X, 사전 순으로 증가하는 순서로 출력

N, M = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = [0 for i in range(M)]
visited = [False for i in range(N)]

def recur(cur):
    if cur == M:
        print(*arr)
        return

    for i in range(N):
        if visited[i] == True:
            continue
        arr[cur] = nums[i]
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0)

