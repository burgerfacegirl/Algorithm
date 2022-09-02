# 1220. magnetic

T = 10

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        # stack = []
        k = 0
        for j in range(N):
            if table[j][i] == 1:
                k = 1
            elif table[j][i] == 2 and k == 1:
                cnt += 1
                k = 0

    print(f'#{tc} {cnt}')