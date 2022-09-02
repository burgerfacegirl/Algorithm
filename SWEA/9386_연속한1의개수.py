# 추가문제 연속한 1의 개수

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int,input()))      # 숫자 리스트로 받음 ([1,0,0,...])
    # num = input()                   # 그냥 string으로 받음 (이럴땐 == 1 이 아니라 =='1'로 검사해야함)
    cnt = 0
    maxV = 0
    for i in range(N):
        if num[i] == 1:
            cnt += 1
            if cnt > maxV:          # 0일때 비교해주면 마지막이 1로 끝날때 maxV 값 갱신 안 됨
                maxV = cnt
        else:
            cnt = 0
    print(f'#{tc} {maxV}')