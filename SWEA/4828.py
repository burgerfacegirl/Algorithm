#min max(제출용)
import sys
sys.stdin = open('4828.txt')
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    maxV = 0
    minV = arr[0]
    for i in range(N):
        if arr[i] > maxV:
            maxV = arr[i]
        if arr[i] < minV:
            minV = arr[i]
    print(f'#{tc} {maxV-minV}')
