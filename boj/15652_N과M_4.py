#221011_boj_15652_N과M(4)

def c(K, start):
    if K == M:
        print(*result)
        return
    else:
        for i in range(start, N):
            result[K] = A[i]
            c(K+1, i)

N, M = map(int,input().split())
A = [i for i in range(1, N+1)]
used = [0] * N
result = [0] * M

c(0, 0)

