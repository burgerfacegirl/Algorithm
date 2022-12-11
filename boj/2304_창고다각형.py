N = int(input())
land = list([0] * 1001 for _ in range(1001))
fac = []

for i in range(N):
    fac.append(list(map(int,input().split())))


fac.sort()

print(fac)
maxH = 0
maxI = 0
for i in range(N):
    if maxH <= fac[i][1]:
        maxH = fac[i][1]
        maxI = i

for k in range(i):


print(maxI)
print(maxH)