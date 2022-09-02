# IM 대비문제

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    danjo = []
    for i in range(N):
        for j in range(i+1, N):
            multi = arr[i] * arr[j]
            new_m = str(multi)
            ans = 0
            for k in range(len(new_m)-1):
                if new_m[k] <= new_m[k+1]:
                    ans += 1
            if ans == len(new_m) - 1:
                danjo.append(multi)

            # new_m = multi
            # sq = 10**(len(str(multi))-1)
            # if sq == 1:
            #     continue
            # cnt = 0
            # for _ in range(len(str(multi))-1):
            #     if (multi%sq)//(sq//10) >= multi//sq:
            #         cnt += 1
            #         multi = multi%sq
            #     sq //= 10
            # if cnt == len(str(new_m)) - 1:
            #     danjo.append(new_m)

    if len(danjo) == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(danjo)}')

