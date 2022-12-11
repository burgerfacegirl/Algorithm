#220912_bog_2644_촌수계산_실버2

import sys
def dfs(A, B):
    q = []
    q.append(A)
    visited[A] = 0
    while q:
        t = q.pop(0)
        # visited[t] = 1
        for w in family[t]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[t] + 1
    # dfs(i)
    # for k in range(1,N+1):
    #     if A in family[k]:
    #         if k == B:
    #             c += 1
    #             return c
    #         else:
    #             for i in family[k]:
    #                 if i == B:
    #                     c += 1
    #                     return c
    #             else:
    #                 c += 1
    #                 dfs(k, B)
    # if c == 0:
    #     c = -1
    #     return c

N = int(sys.stdin.readline())
A, B = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())
family = [[] for _ in range(N+1)]
# visited = [-1] * (N+1)
visited = [-1] * (N + 1)
q = []
q.append(A)
visited[A] = 1

# visited[A] = 0
c = 0
for _ in range(C):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)

dfs(A, B)
print(family)

print(visited)
print(visited[B])