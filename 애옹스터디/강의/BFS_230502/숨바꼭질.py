# boj_숨바꼭질

'''
거리 구하는 세가지 방법
1. 거리 구하는 배열 따로 만든다.(dist[nxt] = disx[cur] + 1)
2. que에 넣을때 거리를 같이 저장해준다. (que.append([nxt, dist + 1])
* 3. depth(깊이)단위로 끊어서 탐색 (size = len(que), for _ in range(size))
(거리 0 인점 다봤으면 멈추고, 1인점 다봤으면 멈추고 -> 큐 사이즈 재서)
(3 => 특정 시점에서 멈추고자 할때 좋음)
'''
# 10만보다 큰 위치로 갔다와도 최단거리면 괜찮음
# 그래서 혹시 모르니까 20만으로 잡는 거

from collections import deque

n, m =map(int, input().split())
visited = [False for i in range(200010)]

que = deque()