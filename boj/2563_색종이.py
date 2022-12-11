# IM 추천문제 boj 2563_색종이

N = int(input())

pan = [[0] * 100 for _ in range(100)]

for i in range(N):
    L, B = map(int,input().split())
    for p in range(9+B, B-1, -1):           # 1로 채우는 거니까 행,열 둘다 마지막 칸 인덱스는 빼야함(그래야 10칸)
        for q in range(L, 10+L):
            pan[p][q] = 1

area= 0
for i in range(100):
    for j in range(100):
        if pan[i][j] == 1:
            area += 1

print(area)