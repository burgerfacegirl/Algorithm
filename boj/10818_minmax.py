# boj 10818

N = int(input())

arr = list(map(int,input().split()))

maxV = -2000000
minV = 2000000
for i in range(N):
    if arr[i] > maxV:
        maxV = arr[i]
    if arr[i] < minV:
        minV = arr[i]

print(f'{minV} {maxV}')
