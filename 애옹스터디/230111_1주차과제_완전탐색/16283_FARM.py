# boj_16538_Farm_완전탐색

# 양이 먹는 사료 양: a , 염소가 먹는 사료 양: b
# 양 + 염소 전체 마리 수: n, 어제 소비한 전체 사료 양: w

a, b, n, w = map(int, input().split())

sheep = []
goat = []

for i in range(1, 1001):       # 양
    for j in range(1, 1001):   # 염소
        if a*i + b*j == w and i+j == n:
            sheep.append(i)
            goat.append(j)

if len(sheep) > 1 or len(sheep) == 0:
    print(-1)
else:
    print(sheep[0], goat[0])