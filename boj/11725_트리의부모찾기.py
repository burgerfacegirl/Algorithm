# 220928_boj_11725_트리의 부모 찾기
import sys
sys.setrecursionlimit(100000)

def find(v):
    if adjList[v]:
        for w in adjList[v]:
            if p[w] == 0 and w != 1:
                p[w] = v
                find(w)

N = int(input())
adjList = [[] for _ in range(N+1)]
p = [0] * (N+1)
c = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int,input().split())
    adjList[a].append(b)
    adjList[b].append(a)

print(adjList)
find(1)
for i in range(2, N+1):
    print(p[i])