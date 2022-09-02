# 추가문제 9367.점점 커지는 당근의 개수

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int,input().split()))

    cnt = 1                             # 커지는 당근의 개수
    maxV = 1                            # 커지는 당근의 개수 중 최댓값
    for i in range(1, N):           
        if carrots[i] > carrots[i-1]:   # 이전 당근이 더 작으면 
            cnt += 1                    # cnt +1
            if maxV < cnt:              # 최댓값 갱신
                maxV = cnt
        else:                           # 이전 당근이 더 작지 않으면
            cnt = 1                     # cnt 1로 초기화

    print(f'#{tc} {maxV}')