def msort(i, N):  # i 병합구간의 시작 인덱스, N 구간의 원소 개수 l = i, r = i+N-1
    global cnt, ans
    if N == 1:  # 분할한 원소가 1개만 남은 경우
        return

    else:
        msort(i, N // 2)  # 병합할 왼쪽 구간의 시작 인덱스
        msort(i + N // 2, N - N // 2)  # 병합할 오른쪽 구간의 시작 인덱스 / 개수로는 N//2 (인덱스로는 N//2-1)

        # 리턴값 없이 i, j=i+N//2 계산으로 가능
        k = 0
        l, r = i, i + N // 2
        while l < i + N // 2 and r < i + N:
            if num[l] <= num[r]:  # 오름차순이면, 작은 숫자 먼저 tmp에 복사
                tmp[k] = num[l]
                l += 1  # 왼쪽 구간에서 선택된 경우 l++
            else:
                tmp[k] = num[r]
                r += 1  # 오른쪽 구간에서 선택된 경우 r++
            k += 1

        while l < (i + N // 2):  # 왼쪽 구간에 남은 숫자가 있으면 모두 tmp에 복사
            tmp[k] = num[l]
            l += 1
            k += 1

        while r < (i + N):  # 오른쪽 구간에 남은 숫자가 있으면 모두 tmp에 복사
            tmp[k] = num[r]
            r += 1
            k += 1

        for k in range(N):  # 병합한 결과를 원본에 다시 복사
            num[i + k] = tmp[k]
            cnt += 1
            if cnt == K:
                print(num[i+k])
                break

        return i


N, K = map(int,input().split())
num = list(map(int,input().split()))

tmp = [0] * N  # 임시 저장소
cnt = 0  # 오른쪽 원소가 먼저 복사되는 경우의 수
ans = 0
msort(0, N)
if cnt < K:
    print(-1)
