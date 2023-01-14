# boj_1469_방 배정하기_완전탐색

A, B, C, N = map(int, input().split())
ans = 0

for i in range(0, 300):
    for j in range(0, 300):
        for k in range(0, 300):
            if (A*i + B*j + k*C) == N:
                ans = 1
                break
    if ans == 1:
        break
print(ans)