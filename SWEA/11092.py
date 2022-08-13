# 최대 최소의 간격

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    minI = maxI = arr[0]
    maxV = minV = arr[0]

    for i in range(len(arr)):
        if minV > arr[i]:
            minV = arr[i]
            minI = i+1
        if maxV <= arr[i]:
            maxV = arr[i]
            maxI = i+1

    ans = maxI - minI
    print(f'#{tc} {-ans}') if ans<0 else print(f'#{tc} {ans}')