# 추가문제 1차원 정원

T = int(input())

for tc in range(1, T+1):
    N, D = map(int,input().split())

    waterd = D*2+1
    ans = 0

    if N % waterd :
        ans = N//waterd + 1
    else:
        ans = N//waterd

    print(f'#{tc} {ans}')