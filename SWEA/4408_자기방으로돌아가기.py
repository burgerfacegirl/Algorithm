# 추가문제 4408. 자기방으로돌아가기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 201
    for _ in range(N):
        now, go = map(int,input().split())
        if now < go:
            for i in range((now+1)//2, (go+1)//2+1):
                cnt[i] += 1
        elif now > go:
            for i in range((go+1)//2, (now+1)//2+1):
                cnt[i] += 1
    maxV = -1
    for i in cnt:
        if i > maxV:
            maxV = i

    print(f'#{tc} {maxV}')