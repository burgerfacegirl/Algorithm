# boj_14400_편의점2

N = int(input())

homes = [list(map(int, input().split())) for _ in range(N)]

homes.sort(key=lambda x: x[0])
x1 = homes[(N-1)//2][0]

homes.sort(key=lambda y: y[1])
y1 = homes[(N-1)//2][1]

answer = 0
for i in range(N):
    answer += abs((homes[i][0]-x1)) + abs((homes[i][1]-y1))
print(answer)