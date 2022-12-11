#220927_boj_4963_섬의개수
# 재귀로 못품(recursion error)

def find(i, j):
    q = []
    q.append((i,j))
    while q:
        i, j = q.pop(0)
        for di, dj in [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1],[0,-1], [-1,-1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<h and 0<=nj<w:
                if mmap[ni][nj] == 1:
                    q.append((ni,nj))
                    mmap[ni][nj] = 0

w = h = 1
while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    mmap = [list(map(int,input().split())) for _ in range(h)]
    island = 0
    # print(mmap)
    for i in range(h):
        for j in range(w):
            if mmap[i][j] == 1:
                island += 1
                find(i,j)
    print(island)