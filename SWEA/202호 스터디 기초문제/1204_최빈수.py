# 1일차 - 최빈수 구하기

T = int(input())

for tc in range(1, T+1):
    tc = int(input())
    arr = list(map(int,input().split()))
    count = [0] * 101            # 카운트 배열 (점수 최댓값 100이니까 101개)

    for i in range(len(arr)):

        count[arr[i]] += 1      # count[각 학생의 점수] 점수를 카운트 배열의 인덱스로 해서 개수 세어줌
    maxI = maxV = 0

    for j in range(101):        # count 배열 값 제일 큰 게 최빈수고, 그 인덱스가 해당 점수니까 인덱스 출력해줌
        if count[j] >= maxV:
            maxV = count[j]
            maxI = j

    print(f'#{tc} {maxI}')



