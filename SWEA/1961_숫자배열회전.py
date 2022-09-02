# 추가문제. 1961_숫자 배열 회전

T = int(input())
# newarr[j][N-1-i]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    newarr = [[[] for _ in range(3)] for _ in range(N)]

    p = -1
    for i in range(N):
        p += 1
        for j in range(N-1,-1,-1):
            newarr[p][0].append(arr[j][i])

    p = -1
    for i in range(N-1, -1, -1):
        p += 1
        for j in range(N-1, -1, -1):
            newarr[p][1].append(arr[i][j])

    p = -1
    for i in range(N-1, -1, -1):
        p += 1
        for j in range(N):
            newarr[p][2].append(arr[j][i])

    print(f'#{tc}')
    for i in newarr:
        for j in i:
            for k in j:
                print(k, end = '')
            print(' ', end='')
        print()
