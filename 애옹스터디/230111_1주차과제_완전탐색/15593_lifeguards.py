# boj_15593_lifeguards_완전탐색

N = int(input())

time = [list(map(int,input().split())) for _ in range(N)]
time.sort()

times = [0 for _ in range(1001)]

for i in range(N):
    for j in range(time[i][0], time[i][1]):
        times[j] += 1

maxV = 0

for i in range(N):
    cnt = 0
    for j in range(time[i][0], time[i][1]):
        times[j] -= 1
    for k in range(1001):
        if times[k] >= 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
    for j in range(time[i][0], time[i][1]):
        times[j] += 1

print(maxV)