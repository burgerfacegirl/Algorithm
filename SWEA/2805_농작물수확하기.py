# 2805_농작물 수확하기


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]

    s = 0

    middle = N//2
    start = end = N//2
    for i in range(N):
        for j in range(start, end+1):
            s += farm[i][j]
        if i < middle:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1


