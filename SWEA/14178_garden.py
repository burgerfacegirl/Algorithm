T = int(input())

for tc in range(1, T+1):
    N, D = map(int,input().split())
    i = 0
    while True:
        if i * (1 + 2 * D ) >= N:
            break
        else:
            i += 1

    print(f'#{tc} {i}')