# 추가문제 10564_이웃한 수의 합

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    minV = 2000000000
    maxV = -2000000000

    for i in range(N-1):
        if arr[i] + arr[i+1] > maxV:
            maxV = arr[i] + arr[i+1]
        if arr[i] + arr[i+1] < minV:
            minV = arr[i] + arr[i+1]

    print(f'#{tc} {maxV} {minV}')