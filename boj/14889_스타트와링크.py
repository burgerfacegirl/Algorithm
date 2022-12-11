# 221020_boj_14889_스타트와 링크

N = int(input())
power = [list(map(int, input().split()))]

def dfs(L, BeginWith):
    # 종료 조건
    if L == r:
        C.append(results)

    else:
        for i in range(BeginWith, len(n)):
            C[L] = [i]
            DFS(L+1, i+1)

r = N/2
C = []
results = []