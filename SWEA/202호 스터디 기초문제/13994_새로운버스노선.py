# problem box_02. 13994. 새로운 버스 노선

T = int(input())

for tc in range(1, T+1):
    cnt = [0] * 1001                               # cnt[정류장 번호]로 버스가 해당 정류장에 서면 +1 해줌
    N = int(input())                               # 노선 수
    for _ in range(N):                             # 노선 별로 버스 종류와 출발 정류장(A), 도착 정류장(B) 받아줌
        what, A, B = map(int,input().split())
        if what == 1:                              # 일반버스
            for i in range(A, B+1):                # 출발지부터 도착지까지 전부 cnt[버스정류장]+1
                cnt[i] += 1

        # 급행, 광역 급행 버스는 출발지, 도착지 먼저 +1(무조건 서니까) / 이미 넣어준 A,B 빼고 홀짝 조건대로 +1
        elif what == 2:                            # 급행버스
            cnt[A] += 1
            cnt[B] += 1
            if A % 2:                              # A 홀수
                for i in range(A+1, B):            
                    if i % 2:
                        cnt[i] += 1
            else:
                for i in range(A+1, B):            
                    if i % 2 == 0:
                        cnt[i] += 1
        elif what == 3:                            # 광역 급행버스
            cnt[A] += 1
            cnt[B] += 1
            if A % 2:                              # A 홀수
                for i in range(A+1, B):             
                    if i % 3 == 0 and i % 10:
                        cnt[i] += 1
            else:
                for i in range(A+1, B):
                    if i % 4 == 0:
                        cnt[i] += 1
    maxV = 0
    for i in cnt:                                  # 각 정류장 별 도착하는 버스 수 중 최댓값 구해줌
        if i > maxV :
            maxV = i

    print(f'#{tc} {maxV}')

