#221010_boj_1359_복권

def factorial(N):
    if N==1 or N==0:
        return 1
    else:
        return N * factorial(N-1)

def nCm(N, M):
    if N>=M:
        return factorial(N)//(factorial(N-M)*factorial(M))
    else:
        return 0


N, M, K = map(int,input().split())
ans = 0

# print((nCm(M, M-K)*nCm(N-M, K))//nCm(N,M))

for i in range(K, M+1):
    ans += nCm(M, K)*nCm(N-M, M-K)

ans = ans/nCm(N, M)
print(ans)