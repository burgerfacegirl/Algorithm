T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ws = list(map(int,input().split()))
    tall = max(ws)
    diff = 0
    cnt = [0] * 300
    ans = 0
    for i in range(N):
        if tall-ws[i] != 0:
            cnt[ws[i]] += 1
            diff += tall-ws[i]

    if cnt[1] != 0:
        ans += cnt[1]*2-1

    diff_0 = diff - cnt[1]

    if diff != 0:
        if cnt[2]*2 == 2 and diff == 2:
            ans = 2
        elif diff_0 < cnt[ans+1]*(ans+1):
            ans = ans
        elif diff_0 >= cnt[ans+1]*(ans+1):
            if diff%3 == 0:
                ans = diff//3*2
            elif diff%3 == 1:
                ans = diff//3*2 + 1
            elif diff%3 == 2:
                ans = diff//3*2 + 2

    else:
        ans = 0

    print(f'#{tc} {ans}')
