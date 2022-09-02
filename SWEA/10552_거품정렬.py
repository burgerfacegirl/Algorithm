# 추가문제 10552. 거품정렬

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    ans = 0
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ans +=1

    print(ans)