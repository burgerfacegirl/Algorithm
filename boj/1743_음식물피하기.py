# 221009_boj_1743_음식물 피하기
import sys
sys.setrecursionlimit(1000000)
def big(i, j):
    global s, maxV
    for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and path[ni][nj] == 1:
            path[ni][nj] = 0
            s += 1
            if maxV < s:
                maxV = s
            big(ni, nj)

N, M, K = map(int,input().split())
maxV = 0

path = list([0] * M for _ in range(N))

for _ in range(K):
    i, j = map(int, input().split())
    path[i-1][j-1] = 1                  # 쓰레기 표시


for i in range(N):
    for j in range(M):
        if path[i][j] == 1:             # 쓰레기 있으면
            path[i][j] = 0              # 그 자리 0으로 바꾸고 (방문 표시)
            s = 1                       # 쓰레기 크기 1로 초기화 후 함수 호출 (상하좌우 쓰레기 크기 세줌)
            big(i,j)
print(maxV)