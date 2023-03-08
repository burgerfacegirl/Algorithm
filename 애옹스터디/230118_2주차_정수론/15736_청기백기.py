# boj_15736_청기 백기_정수론

N = int(input())

ans = 0
for i in range(1, int(N**0.5)+1):
    if i*i <= N:
       ans += 1

print(ans)

