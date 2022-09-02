# 최댓값과 최솟값의 차이 구하기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    maxV = minV = arr[0]            # 최댓값, 최솟값 변수
    for i in range(1, len(arr)):
        if arr[i] >= maxV:          # maxV 보다 크거나 같으면 maxV값 arr[i]로 바꿔줌
            maxV = arr[i]
        if arr[i] <= minV:          # minV 보다 작거나 같으면 minV값 arr[i]로 바
            minV = arr[i]

    print(f'#{tc} {maxV-minV}')