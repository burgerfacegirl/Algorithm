# 220808_List1. 1206. View

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    cnt = 0
    for i in range(2, N-2):
        maxF = 0
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            if maxF < arr[i-2]:
                maxF = arr[i-2]
            if maxF < arr[i-1]:
                maxF = arr[i-1]
            if maxF < arr[i+1]:
                maxF = arr[i+1]
            if maxF < arr[i+2]:
                maxF = arr[i+2]
            cnt += arr[i] - maxF

    print(f'#{tc} {cnt}')
