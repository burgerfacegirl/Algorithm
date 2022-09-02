# 추가문제 5789.현주의 상자 바꾸기

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0]*N                         # 배열 0으로 초기화

    for i in range(Q):
        L, R = map(int,input().split())
        for k in range(L-1,R):          # arr index는 0부터니까 범위 1씩 빼줌
            arr[k] = i+1                # i 0부터니까 1 더해줌

    print(f'#{tc}', end = ' ')
    print(*arr)



