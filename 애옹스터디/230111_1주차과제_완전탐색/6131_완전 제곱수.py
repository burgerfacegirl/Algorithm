# boj_6131_완전 제곱수
N = int(input())
# 1 <= B <= A <= 500
cnt = 0
for b in range(1, 501):
    for a in range(b, 501):
        if a**2 == b**2 + N:
            cnt += 1

print(cnt)