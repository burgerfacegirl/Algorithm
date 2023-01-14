# boj_14568_2017 연세대학교 프로그래밍 경시대회

N = int(input())

cnt = 0
for i in range(1, N+1):         # 남규
    for j in range(1, N+1):     # 영훈
        for k in range(1, N+1): # 택희
            if i+j+k != N:
                continue
            if i < 2+j :
                continue
            if k%2:
                continue
            cnt += 1
print(cnt)

