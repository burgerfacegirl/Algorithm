# boj_숨바꼭질

# 예제코드만 
# 역추적도 가능함 연습해보기
import heapq

n, m = map(int, input().split())
s = int(input())
v = [[] for i in range(n + 1)]
dist = [1000000000 for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())

    v[a].append([b, c])

pq = []

heapq.heappush(pq, [0, s])
dist[s] = 0
while len(pq) > 0:
    cur = pq[0][1]
    d = pq[0][0]
    heapq.heappop(pq)

    if dist[cur] != d:
        continue

    for i in v[cur]:
        nxt = i[0]
        nd = d + i[1]

        if dist[nxt] <= nd:
            continue

        dist[nxt] = nd
        heapq.heappush(pq, [nd, nxt])

for i in range(1, n + 1):
    if dist[i] == 1000000000:
        print("INF")
    else:
        print(dist[i])