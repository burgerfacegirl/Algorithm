# 202호 스터디 problem2 2001. 파리퇴치

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for p in range(M):
                for q in range(M):
                    s += arr[i+p][j+q]
            if maxV < s:
                maxV = s

    print(f'#{tc} {maxV}')
