# 전기버스
from calendar import c
import sys
sys.stdin = open('4831.txt')

T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    chargingS = list(map(int,input().split()))
    print(chargingS)
    stations = [0] * N
    position = 0
    ans = 0
    # for idx in range(len(chargingS)-1):
    #     if chargingS[idx+1]-chargingS[idx] > K:
    #         print(0)
    #         break
    #     else:
    #         pass

    while True:
        for i in range(position+K, position, -1):
                if i in chargingS:
                    position = i
                    ans += 1
        print(ans)
        break