# 볼링공 고르기

N, M = map(int,input().split())

balls = list(map(int,input().split()))
cnt = [0] * (M+1)                       # 무게별 공 개수
ans = 0

for i in balls:
    cnt[i] += 1

for i in range(1, M+1):
    ans += cnt[i]*sum(cnt[i+1:M+2])     # 경우의 수 세줌 (본인 공 개수 * 무게별 공 개수)

print(ans)
