# 221102_1966_프린터 큐_구현

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    ims = list([_] for _ in input().split())
    ims2 = []
    for i in ims:
        ims2.append(int(i[0]))
    q = []
    ans = 0
    for i in range(N):
        if i == M:
            ims[i].append('a')
        else:
            ims[i].append('x')

    for i in ims:
        i[0] = int(i[0])

    i = 0
    hi = True
    while hi:
        maxV = max(ims2)
        if ims[0][0] == maxV:
            ans += 1
            if ims[0][1] == 'a':
                print(ans)
                hi = False
                break
            else:
                ims.pop(0)
                ims2.pop(ims2.index(maxV))  # ims2에서도 해당 값 pop해주기
        else:
            ims.append(ims.pop(0))





