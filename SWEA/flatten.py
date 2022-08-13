#평탄화 문제

import sys
sys.stdin = open('flatten.txt')

T = 10 # 테스트 케이스 10으로 고정돼있음

for tc in range(1, T+1): # 테스트 케이스 동안
    N = int(input()) # 정해진 덤프 횟수
    arr = list(map(int,input().split())) # 상자들의 높이를 리스트로 받아줌
    maxH = minH = arr[0] # 높이들 중 최댓값, 최솟값 받기 위해 변수 생성
    maxI = minI = 0 # 높이들 중 최댓값, 최솟값의 index를 받아오기 위해 변수 생성
    # 덤프 1회 후 최솟값에 1 더하고 최댓값에 1 빼준 값 그 자리에 업데이트 해주기 위해 index도 받아옴
    # -> 그 상태로 다시 덤프해줘야 하니까.
    while N > 0: # 덤프 횟수가 0이 될때까지
        for idx in range(len(arr)): # arr 전부 돌면서
            if maxH < arr[idx]:
                maxH = arr[idx]
                maxI = idx
            if minH > arr[idx]:
                minH = arr[idx]
                minI = idx      # 최댓값, 최솟값과 그 index 찾아줌
        minH = minH + 1
        maxH = maxH - 1
        arr[maxI] = maxH 
        arr[minI] = minH # 1회 덤프 후 값 arr에 업데이트 해주고
        N -= 1 # 덤프 횟수 한번 빼고 다시 반복문 돔
        if max(arr)-min(arr) <= 1: # 덤프 횟수가 남았더라도 평탄화가 완료되면 
            break # 반복문을 빠져나가 그때의 최댓값과 최솟값을 반환한다.
    print(f'#{tc} {max(arr)-min(arr)}') 