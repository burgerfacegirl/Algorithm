# 추가문제 6019. 기차 사이의 파리

T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int,input().split())
    print(f'#{tc} {(D//(A+B))*F + ((D%(A+B))/(A+B))*F}')

# 방법2 - 더 간단
#
# for T in range(1,int(input())+1):
#     D,A,B,F=map(int,input().split())
#     print(f'#{T}',D/(A+B)*F) 