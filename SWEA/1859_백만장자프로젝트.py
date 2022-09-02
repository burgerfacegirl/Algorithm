# 추가문제 1859.백만장자프로젝트

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))

    profit = 0
    hi = True
    while hi:
        maxV = maxI = 0
        for i in range(N):
            if price[i] > maxV:
                maxV = price[i]                 # 최고 매매가
                maxI = i                        # 최고 매매가인 날

        for k in range(maxI+1):                 # 최고 매매가인 날 이전까지의 모든 매매가 빼서 profit에 더해줌
            if price[k] > 0:
                profit += price[maxI] - price[k]
                price[k] = 0                    # 최고 매매가인 날 이전까지의 모든 매매가 0으로 초기화

        rest = 0
        for q in range(maxI+1,N-1):             # 뒤의 값들 중 이익을 얻을 수 있는 경우가 남아있는지 확인
            if price[q] < price[q+1]:
                rest += 1                       # 이익을 얻을 수 있는 경우 남아있다면 반복문 다시
        if rest == 0:                           # 남은 날 중 모든 q일의 매매가가 q+1일의 매매가보다 작지 않으면
            hi = False                          # 반복문 종료

    print(f'#{tc} {profit}')
