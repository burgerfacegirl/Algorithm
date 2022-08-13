from calendar import c
import sys
sys.stdin = open('4831.txt')

T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    chargingS = list(map(int,input().split()))
    position = 0
    ans = 0
    while position + K <= N:
        # for idx in range(len(chargingS)-1):
        #     if chargingS[idx+1]-chargingS[idx] > K:
        #         print(0)
        #         break
        # for i in range(K, 0, -1):
        #     if (position+i) in chargingS:
        #         position += i
        #         ans += 1
        #         break          
        # else:
        #     ans = 0
        #     break
            
        for i in range(position+K, position, -1):
            if i in chargingS:
                position = i
                ans+=1
                break
        else:
            ans=0
            break
    print(f'#{tc} {ans}')
    