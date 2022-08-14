# 거품정렬
T = int(input())


for tc in range(1, T+1):
    N = int(input())    # 주어지는 정수 개수
    arr = list(map(int,input().split()))   # 정수들 리스트에 담아줌
    cnt = 0
    for i in range(0,N):    # 정렬 범위
        for j in range(0,N-1):     # 맨 뒷자리 정렬된 숫자 빼고 범위 줄여주며 비교
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # 앞 숫자가 더 크면 뒤 숫자랑 자리 바꿔줌
                cnt += 1
    print(f'#{tc} {cnt}')