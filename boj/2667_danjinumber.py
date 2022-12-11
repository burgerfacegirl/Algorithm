#220919_boj_2667_단지번호붙이기_DFS,BRS_실버1

def dfs(i, j):
    cnt = 1
    stack = []
    visited[i][j] = 1                           # 시작 정점 방문표시
    while True:
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:           # 시작 정점(v)에 인접한 집(w) 찾기
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and map[ni][nj] == 1 and visited[ni][nj] == 0:      # 인접한 집(w) 있으면
                stack.append((i, j))            # stack에 넣고
                i, j = ni, nj                   # v <- w
                visited[i][j] = 1               # 인접한 집 방문 표시
                cnt += 1                        # 집의 수 +1
                break                           # 인접한 집을 기준으로 다시 4방위 검사
        else:                                   # w가 없으면
            if stack:
                i, j = stack.pop()              # 스택에 지나온 칸이 남은 경우
            else:
                break
    cnt_list.append(cnt)

N = int(input())
map = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt_list = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and visited[i][j] == 0:    # 집이 있고(1이고) 방문 안 했으면
            dfs(i, j)

print(len(cnt_list))
cnt_list.sort()
for i in cnt_list:
    print(i)

# 재귀
def dfs(a,b):
    global cnt
    cnt+=1
    #방문한 집은 배열에서 2로 바꿔서 다시 안오게 함
    arr[a][b]=2
    for y,x in d:       # 좌 우 상 하
        if 0<=a+x<N and 0<=b+y<N and arr[a+x][b+y]==1:
            dfs(a+x,b+y)

#상하좌우
d=[[-1,0],[1,0],[0,-1],[0,1]]
ans=[]
N=int(input())
arr=[list(map(int,input())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        cnt=0
        if arr[i][j]==1:
            dfs(i,j)
            #단지 내 집의 수 출력
            ans.append(cnt)
#단지 수 출력
print(len(ans))
#단지 내 집의 수 오름차순으로 출력
ans.sort()
for h in ans:
    print(h)