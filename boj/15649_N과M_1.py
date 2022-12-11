#221010_boj_15649_N과M(1)

def p(K):               # K 현재 단계, M 종료 조건(다 뽑았을 때)
    if K == M:
        print(*result)
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                result[K] = A[i]
                p(K+1)
                used[i] = 0


N, M = map(int,input().split())
A = [i for i in range(1,N+1)]
used = [0] * N
result = [0] * M

p(0)