# boj_2792_보석상자
import sys

N, M = map(int, sys.stdin.readline().split())

colors = [0] * M
sum_colors = 0
for i in range(M):
    colors[i] = int(sys.stdin.readline())
    sum_colors += colors[i]

colors.sort()
s = sum_colors // N
while True:
    check_c = 0  # 보석을 가진 학생 수
    for j in range(M-1, -1, -1):
        if colors[j] % s == 0:
            check_c += colors[j] // s
        else:
            check_c += colors[j] // s + 1
        if check_c > N:
            break
    if check_c == N:
        break
    elif check_c > N:
        s += 1
    else:
        s -= 1

print(s)