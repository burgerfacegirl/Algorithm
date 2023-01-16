# boj_2304_창고 다각형_완전탐색

N = int(input())
containers = []
H = []

for _ in range(N):
    containers.append(list(map(int,input().split())))

containers.sort()
for i in range(N):
    H.append(containers[i][1])
maxH = max(H)
cnt = 0

for container in containers:
    if container[1] == maxH:
        maxL = container[0]
        l = maxL
        r = maxL + 1
        lcs = containers[0:l]
        rcs = containers[r:N]
        cnt += maxH
        container[0] = 0
        container[1] = 0
    break

while True:
    maxHl = max()
print(containers)
