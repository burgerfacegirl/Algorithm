
N = int(input())
stones = list(map(int,input().split()))

checks = []
check = 0
maxL = 0
#L 체크
for i in range(0, N):
    if stones[i] == 1:
        check += 1
        if maxL < check:
            maxL = check
    else:
        check = 0

check = 0
maxR = 0
#R 체크
for j in range(0, N):
    if stones[j] == 2:
        check += 1
        if maxR < check:
            maxR = check
    else:
        check = 0
print(max(maxL, maxR))